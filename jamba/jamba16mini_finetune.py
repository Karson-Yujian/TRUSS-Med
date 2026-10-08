import os
import torch
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, logging
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig

# 设置日志级别
logging.set_verbosity_info()
logger = logging.get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Fine-tune AI21-Jamba model on medical dataset")
    parser.add_argument("model_name", type=str, default="AI21-Jamba-Mini-1.6",
                        help="Model name under /work/home/acbjfbaxkm/AI21Labs/")
    parser.add_argument("dataset_path", type=str, default="RAG_MedQA_USS_test_train.json",
                        help="Dataset path under /work/home/acbjfbaxkm/DataSet/")
    # 移除了 output_prefix 参数
    args = parser.parse_args()

    # 构建完整路径
    model_path = os.path.join("/work/home/acbjfbaxkm/AI21Labs/", args.model_name)
    dataset_path = os.path.join("/work/home/acbjfbaxkm/DataSet/", args.dataset_path)

    # 使用 model_name 作为顶级目录
    dataset_name = os.path.splitext(os.path.basename(args.dataset_path))[0]
    output_dir = os.path.join("/work/home/acbjfbaxkm/Jamba-Test/finetune_result",
                              f"{args.model_name}/{dataset_name}")  # 修改了目录结构
    logging_dir = os.path.join(output_dir, "logs")

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(logging_dir, exist_ok=True)

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",  # 注释掉自动分配
        torch_dtype=torch.bfloat16,
        # attn_implementation="flash_attention_2",
        use_cache=False  # 显式设置 use_cache 为 False
    )

    lora_config = LoraConfig(
        r=8,
        target_modules=[
            "embed_tokens",
            "x_proj", "in_proj", "out_proj",  # mamba
            "gate_proj", "up_proj", "down_proj",  # mlp
            "q_proj", "k_proj", "v_proj", "o_proj",  # attention
        ],
        task_type="CAUSAL_LM",
        bias="none",
    )

    # 加载自定义数据集
    logger.info(f"Loading dataset from {dataset_path}")
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    # 定义训练参数
    training_args = SFTConfig(
        output_dir=output_dir,  # 训练过程中模型检查点和最终模型的保存目录
        logging_dir=logging_dir,  # 训练日志(如TensorBoard或CSV日志)的保存目录
        num_train_epochs=2,  # 完整训练数据集的迭代次数
        per_device_train_batch_size=2,  # 每个GPU/TPU核心或CPU上的训练批次大小
        learning_rate=5e-4,  # Adam优化器的初始学习率
        logging_steps=10,  # 每多少训练步骤记录一次日志
        gradient_checkpointing=True,  # 是否使用梯度检查点以节省内存(以计算速度为代价)
        max_seq_length=4096 * 2,  # 输入序列的最大长度，超过此长度的序列将被截断
        save_steps=100,  # 每多少训练步骤保存一次模型检查点
    )

    # 初始化训练器
    trainer = SFTTrainer(
        model=model,
        #processing_class=tokenizer,
        args=training_args,
        peft_config=lora_config,
        train_dataset=dataset,
    )

    try:
        trainer.train()
    except Exception as e:
        logger.error(f"Training failed: {e}")

    # 保存模型
    trainer.save_model()


if __name__ == "__main__":
    main()
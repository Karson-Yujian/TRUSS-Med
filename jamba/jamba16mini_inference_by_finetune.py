import time
import json
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import torch
import re
import logging
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import os
import argparse
from shutil import copy2

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 固定路径部分
fixed_path = "/work/home/acbjfbaxkm/AI21Labs"
dataset_path = "/work/home/acbjfbaxkm/DataSet/"
temperature = 0.85
top_k = 20
top_p = 0.75
number_gpus = 2
# 微调后的结果固定路径部分
peft_fixed_path = "/work/home/acbjfbaxkm/Jamba-Test/finetune_result"

def merge_model(model_path, peft_relative_path):
    """
    合并基础模型和Peft模型

    Returns:
        str: 合并后模型的路径，合并失败时返回None
    """
    # 在现有目录下新增一个合并目录
    merged_dir = "merged"
    peft_model_path = os.path.join(peft_fixed_path, peft_relative_path, merged_dir)

    # 判断是否已经合并
    if os.path.exists(peft_model_path) and os.listdir(peft_model_path):
        logging.info(f"模型已经合并，直接使用合并后的模型: {peft_model_path}")
        return peft_model_path

    try:
        logging.info(f"开始加载基础模型: {model_path}")
        base_model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="auto"
        )

        # 原Peft模型路径
        original_peft_model_path = os.path.join(peft_fixed_path, peft_relative_path)
        logging.info(f"开始加载Peft模型: {original_peft_model_path}")
        model = PeftModel.from_pretrained(base_model, original_peft_model_path)

        logging.info("开始合并模型")
        merged_model = model.merge_and_unload()

        logging.info(f"保存合并后的模型到: {peft_model_path}")
        merged_model.save_pretrained(peft_model_path)

        # 复制分词器文件到合并目录
        logging.info("复制分词器文件到合并目录")

        # 从基础模型目录复制分词器文件
        tokenizer_files = [
            "tokenizer_config.json",
            "special_tokens_map.json",
            "tokenizer.model",
            "vocab.json",
            "merges.txt"
        ]

        for file in tokenizer_files:
            src_file = os.path.join(model_path, file)
            dst_file = os.path.join(peft_model_path, file)

            if os.path.exists(src_file):
                copy2(src_file, dst_file)
                logging.info(f"复制 {file} 到 {peft_model_path}")
            else:
                logging.warning(f"未找到 {file} 文件，跳过复制")

        return peft_model_path
    except Exception as e:
        logging.error(f"合并模型时出错: {e}")
        return None

def load_model_and_tokenizer(model_path):
    """
    加载模型和分词器

    Returns:
        tuple: 包含LLM模型和分词器的元组，加载失败时返回None
    """
    try:
        logging.info(f"开始加载合并后的模型: {model_path}")

        llm = LLM(model=model_path, max_model_len=200 * 1024, tensor_parallel_size=number_gpus)

        logging.info(f"开始加载分词器: {model_path}")
        tokenizer = AutoTokenizer.from_pretrained(model_path)

        logging.info("模型和分词器加载完成")

        return llm, tokenizer
    except Exception as e:
        logging.error(f"加载模型或分词器时出错: {e}")
        return None, None

def generate_response(model, tokenizer, messages):
    """
    根据输入消息生成回复

    Args:
        model (LLM): 加载好的模型
        tokenizer (AutoTokenizer): 加载好的分词器
        messages (list): 输入的消息列表

    Returns:
        str: 生成的回复文本，出错时返回None
    """
    try:
        # 过滤掉助手回复，只保留用户和系统消息
        valid_messages = [msg for msg in messages if msg.get("role") != "assistant"]

        # 构建提示模板
        prompt = tokenizer.apply_chat_template(valid_messages, add_generation_prompt=True, tokenize=False)

        # 设置采样参数
        sampling_params = SamplingParams(
            max_tokens=20 * 1024,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )

        # 生成回复
        outputs = model.generate(prompt, sampling_params=sampling_params)
        text = outputs[0].outputs[0].text

        logging.info(f"生成内容: {text}")
        logging.info(f"-------------------------------------------------------end--------------------------------------------------------------")
        return text
    except Exception as e:
        logging.error(f"生成回复时出错: {e}")
        return None

def process_examples(model, tokenizer, examples, batch_index, batch_size, total_examples, correct_count):
    """
    处理一批示例并生成结果

    Args:
        model (LLM): 加载好的模型
        tokenizer (AutoTokenizer): 加载好的分词器
        examples (list): 示例列表
        batch_index (int): 当前批次索引
        batch_size (int): 批次大小
        total_examples (int): 总示例数
        correct_count (int): 已正确预测的数量

    Returns:
        tuple: 包含结果列表和更新后的正确预测数量的元组
    """
    results = []
    for i, example in enumerate(examples):
        answer_idx = example.get("answer_idx")
        messages = example.get("messages")

        if messages:
            # 生成回复
            generated_text = generate_response(model, tokenizer, messages)

            # 提取预测选项并判断是否正确
            predicted_option = extract_predicted_option_by_us(generated_text)
            is_correct = predicted_option is not None and answer_idx is not None and predicted_option.upper() == answer_idx.upper()

            # 提取问题和系统内容
            question = next((msg.get("content") for msg in messages if msg.get("role") == "user"), None)

            # 更新进度和统计信息
            current_index = batch_index * batch_size + i
            if is_correct:
                correct_count += 1
            accuracy = correct_count / (current_index + 1)

            # 记录详细日志
            logging.info(
                f"进度: {current_index + 1}/{total_examples} ({(current_index / total_examples) * 100:.2f}%), "
                f"预测选项: {predicted_option}, 正确选项: {answer_idx}, 是否正确: {is_correct}, "
                f"准确率: {accuracy:.4f}"
            )

            # 保存结果
            results.append({
                "Question": question,
                "Correct Answer": answer_idx.upper() if answer_idx else None,
                "Predicted Option": predicted_option.upper() if predicted_option else None,
                "Generated Text": generated_text,
                "Correct": is_correct
            })

    return results, correct_count

def extract_predicted_option_by_us(text):
    # 定义数字到字母的映射
    number_to_letter = {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E'
    }
    if not isinstance(text, str):
        return None

    # 定义可能的答案格式的正则表达式模式
    patterns = [
        r'(Answer:|#Answer#|The answer is|Answer is|The correct answer is|Correct answer:|Final answer:)\s*(?:is\s*)?([A-G1-6])',
        # 格式1: ### Answer:**E. Rectal suction biopsy**
        r'### Answer:\*\*?([A-E])\.',
        # 格式2: ### Answer:E. Opioid overdose
        r'### Answer:([A-E])\.',
        # 格式3: ### Answer: 新行 **C. CT scan** 新行
        r'### Answer:\s*\n\s*\*\*([A-E])\.',
        # 格式4: ### Answer: 新行 **1. A. Plummer-Vinson syndrome** 新行
        r'### Answer:\s*\n\s*\*\*\d+\.\s*([A-E])\.',
        # 格式5: **Answer:** 新行 1. A. Aldose reductase
        r'\*\*Answer:\*\*\s*\n\s*\d+\.\s*([A-E])\.',
        # 格式6: **Answer:** 新行 B. Adhesive capsulitis
        r'\*\*Answer:\*\*\s*\n\s*([A-E])\.',
        # 格式7: Answer: Option number 3.
        r'Answer:\s*Option\s*number\s*([1-5])\.',
        # 格式8: ### Answer: 新行 **1. Abnormal expression...** (无选项字母，仅题号)
        r'### Answer:\s*\n\s*\*\*(\d+)\.\s*',
        # 格式9: **Answer:** 新行 1. Abnormal expression... (无选项字母，仅题号)
        r'\*\*Answer:\*\*\s*\n\s*(\d+)\.\s*',
        # 格式10: ### Final Answer: 新行 A. Pancreatic adenocarcinoma
        r'### Final Answer:\s*\n\s*([A-E])\.',
        # 格式11: ### Answer: 新行 Option A.
        r'### Answer:\s*\n\s*Option\s*([A-E])\.',
        # 格式12: ### Answer: 新行 Option number: **D. All**
        r'### Answer:\s*\n\s*Option\s*number:\s*\*\*([A-E])\.',
        # 格式13: ### Answer: 新行 The correct answer is: 新行 A. ACA
        r'### Answer:\s*\n\s*The correct answer is:\s*\n\s*([A-E])\.',
        # 格式14: ### Answer: 新行 Option number is **D. Mask with reservoir**
        r'### Answer:\s*\n\s*Option\s*number\s*is\s*\*\*([A-E])\.',
        # 格式15: ### Answer: 新行 Option A: **Amoxicillin** is commonly
        r'### Answer:\s*\n\s*Option\s*([A-E]):\s*\*\*',
        # 格式16: Answer: Option 1 (EACA)
        r'Answer:\s*Option\s*([1-5])\s*\(',
        # 格式17: ### Answer: 新行 Option 2.
        r'### Answer:\s*\n\s*Option\s*([1-5])\.',
        # 格式18: ### Answer: 新行 Option number **A**.
        r'### Answer:\s*\n\s*Option\s*number\s*\*\*([A-E])\.\*\*',
        # 格式19: ### Answer: 新行 **Option 1: Mesiobuccal cusp...**
        r'### Answer:\s*\n\s*\*\*Option\s*([1-5]):',
        # 格式20: ### Answer: 新行 Option A is correct.
        r'### Answer:\s*\n\s*Option\s*([A-E])\s*is\s*correct\.',
        # 格式21: ### Answer: 新行 Option number: **B**
        r'### Answer:\s*\n\s*Option\s*number:\s*\*\*([A-E])\*\*',
        # 格式22: ### Answer: 新行 Option number 1: **A. Optic neuritis**
        r'### Answer:\s*\n\s*Option\s*number\s*([1-5]):\s*\*\*([A-E])\.',
        # 格式23: ### Answer: 新行 Option number: 4
        r'### Answer:\s*\n\s*Option\s*number:\s*([1-5])',
        # 格式24: ### Answer: 新行 **Option 1**
        r'### Answer:\s*\n\s*\*\*Option\s*([1-5])\*\*',
        # 格式25: ### Answer: 新行 Option **D. Nucleic acids**
        r'### Answer:\s*\n\s*Option\s*\*\*([A-E])\.',
        # 格式26: ### Answer: 新行 Option 1: Herbal medication...
        r'### Answer:\s*\n\s*Option\s*([1-5]):',
        # 格式27: ### Answer: 新行 **Option B: Atropine**（带冒号和内容）
        r'### Answer:\s*\n\s*\*\*Option\s*([A-E]):',
        # 格式28: **Answer:** 新行 Option D.（无冒号，纯字母选项）
        r'\*\*Answer:\*\*\s*\n\s*Option\s*([A-E])\.?',

        # 格式29: **Answer:** 新行 **Option D**（带双星号包裹）
        r'\*\*Answer:\*\*\s*\n\s*\*\*Option\s*([A-E])\*\*',

        # 格式30: **Answer:** 新行 Option 1: **Collagenase**（数字选项带冒号）
        r'\*\*Answer:\*\*\s*\n\s*Option\s*([1-5]):',

        # 格式31: **Answer:** 新行 Option **C. Student's T-test**（带内容的字母选项）
        r'\*\*Answer:\*\*\s*\n\s*Option\s*\*\*([A-E])\.',
        # 格式32: ### Answer: 新行 **Option 2 (Division)**（数字选项带括号说明）
        r'### Answer:\s*\n\s*\*\*Option\s*([1-5])\s*\(',

        # 格式33: Answer: 新行 Option A.（无分隔符，纯字母选项）
        r'Answer:\s*\n\s*Option\s*([A-E])\.?',

        # 格式34: ### Answer: 新行 **Option number: C. PMA...**（带冒号和内容）
        r'### Answer:\s*\n\s*\*\*Option\s*number:\s*([A-E])\.',

        # 格式35: ### Answer: 新行 **Option A**: ...（带冒号和说明）
        r'### Answer:\s*\n\s*\*\*Option\s*([A-E]):',

        # 格式36: ### Answer: 新行 **Option D (Either AB)**（带括号说明）
        r'### Answer:\s*\n\s*\*\*Option\s*([A-E])\s*\(',

        # 格式37: ### Answer: 新行 **Option C**（纯字母选项带双星号）
        r'### Answer:\s*\n\s*\*\*Option\s*([A-E])\*\*',

        # 格式38: Answer: Option A (Safety)（无特殊符号，带括号说明）
        r'Answer:\s*Option\s*([A-E])\s*\(',

        # 格式39: ### Answer: 新行 **Option B. 50**（字母选项带点和数字）
        r'### Answer:\s*\n\s*\*\*Option\s*([A-E])\.',

        # 格式40: **Answer:** 新行 Option **B**（两端带双星号）
        r'\*\*Answer:\*\*\s*\n\s*Option\s*\*\*([A-E])\*\*',

        # 格式46: Answer: Option A（纯字母选项，无标点）
        r'Answer:\s*Option\s*([A-E])',

        # 格式47: **Answer:** **Option A**（双星号包裹选项）
        r'\*\*Answer:\*\*\s*\*\*Option\s*([A-E])\*\*',

        # 格式48: Answer: **C**（仅字母带双星号）
        r'Answer:\s*\*\*([A-E])\*\*',

        # 格式49: Answer: 新行 Option 2（数字选项）
        r'Answer:\s*\n\s*Option\s*([1-5])',

        # 格式50: Answer: Option C.（字母选项带句点）
        r'Answer:\s*Option\s*([A-E])\.',

        # 格式51: **Answer**: Option A: ...（选项带冒号说明）
        r'\*\*Answer:\s*Option\s*([A-E]):',

        # 格式52: **Answer:** Option D.（普通格式带句点）
        r'\*\*Answer:\*\*\s*Option\s*([A-E])\.',

        # 格式53: Answer: **Option B**（带双星号的Option+字母）
        r'Answer:\s*\*\*Option\s*([A-E])\*\*',

        # 格式54: Answer: **C. Fissure burr**（带内容的字母选项）
        r'Answer:\s*\*\*([A-E])\.',

        # 格式55: **Answer:** D.（纯字母加句点）
        r'\*\*Answer:\*\*\s*([A-E])\.',

        # 格式56: **Answer:** 新行 **B. Ordinal**（双星号包裹的字母选项）
        r'\*\*Answer:\*\*\s*\n\s*\*\*([A-E])\.',

        r'Therefore, the answer to the above question is:\s*\n\s*([A-E])\.',
        r'Therefore, the correct answer is:\s*([A-E])\.',

        r'The correct answer,\s*([A-E]),',

        r'Therefore, the answer to the above question is:\s*([A-E])\.',
        r'Therefore, the correct answer is\s*([A-E])\.'

        # 新增格式: "The correct answer is B. Cocaine."
        r'The correct answer is\s*([A-E])\.',
        # 新增格式: "The correct answer is: C. Surgical site infection"
        r'The correct answer is:\s*([A-E])\.',
    ]

    # 尝试每种模式匹配
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL | re.MULTILINE)
        if match:
            answer = match.group(1).strip()
            # 如果匹配到数字，转换为对应的字母
            if answer in number_to_letter:
                return number_to_letter[answer]
            return answer[0].upper() if answer else None

    return None

def main(model_name, dataset_filenames, peft_relative_path):
    """主函数，协调模型加载、数据处理和结果保存"""
    # 构建完整的模型路径
    model_path = os.path.join(fixed_path, model_name)

    # 合并模型
    merged_model_path = merge_model(model_path, peft_relative_path)
    if not merged_model_path:
        return

    # 加载合并后的模型和分词器
    model, tokenizer = load_model_and_tokenizer(merged_model_path)
    if not model or not tokenizer:
        return

    for dataset_filename in dataset_filenames:
        dataset = os.path.join(dataset_path, dataset_filename)

        # 加载数据集
        try:
            logging.info(f"开始加载数据集: {dataset}")
            # 仅支持JSON格式
            with open(dataset, 'r', encoding='utf-8') as f:
                data = json.load(f)

            logging.info(f"数据集加载完成，共{len(data)}个样本")
        except Exception as e:
            logging.error(f"加载数据集时出错: {e}")
            return

        # 初始化结果列表和计数器
        results = []
        batch_size = 8
        num_batches = (len(data) + batch_size - 1) // batch_size
        correct_count = 0
        start_time = time.time()

        logging.info(f"开始推理，批次大小: {batch_size}，总批次: {num_batches}")
        for i in tqdm(range(0, len(data), batch_size), desc="推理进度", total=num_batches):
            batch = data[i:i + batch_size]
            batch_results, correct_count = process_examples(
                model, tokenizer, batch, i // batch_size, batch_size, len(data), correct_count
            )
            results.extend(batch_results)

            # 释放GPU缓存
            torch.cuda.empty_cache()

        # 保存结果
        if results:
            # 生成结果文件名
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

            # 提取数据集文件名（不含扩展名）
            dataset_basename = os.path.basename(dataset)
            dataset_name = os.path.splitext(dataset_basename)[0]

            # 提取checkpoint信息
            checkpoint_info = peft_relative_path.split('/')[-1]

            file_name = os.path.join(
                'results',
                f'jamba16mini_inference_{checkpoint_info}_{model_name}_{dataset_name}_temperature{int(temperature * 100)}_topp{int(top_p * 100)}_topk{top_k}_{current_time}.xlsx'
            )

            # 保存到Excel
            df = pd.DataFrame(results)
            logging.info(f"保存结果到: {file_name}")
            df.to_excel(file_name, index=False)

            # 计算并打印总统计信息
            end_time = time.time()
            total_time = end_time - start_time
            accuracy = correct_count / len(data)

            logging.info(f"推理完成，总样本数: {len(data)}, 正确数: {correct_count}, 准确率: {accuracy:.4f}")
            logging.info(f"总耗时: {total_time:.2f}秒")
        else:
            logging.warning("未收集到任何结果")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run inference with a specified model.')
    parser.add_argument('model_name', type=str, default="AI21-Jamba-Mini-1.6", help='Name of the model to use.')
    parser.add_argument('dataset_filenames', type=str, default="MedMCQA/result/Med_MCQA_knowledge_test.json", nargs='+', help='Dataset paths (for example, an absolute path under data/MedQA or data/MedMCQA).')
    parser.add_argument('peft_relative_path', type=str, default="AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300", help='Relative path of the Peft model (for example, AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300).')
    args = parser.parse_args()

    main(args.model_name, args.dataset_filenames, args.peft_relative_path)

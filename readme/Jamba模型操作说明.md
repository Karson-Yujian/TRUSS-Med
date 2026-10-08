Jamba模型调试说明

1.构建数据集

## 项目环境依赖

项目主要依赖于阿里云环境下conda环境
```bash
conda activate llama_factory
```
完整的包依赖参考[./requirements.txt](./requirements.txt)

### 硬件与系统级驱动依赖

其中硬件与驱动依赖：
| 软件包/硬件        | 版本号/配置     | 备注   |
| ------------ | -------    | ------- | 
| 系统       | Ubuntu 20.04.1 LTS |    |
| CPU       | Intel(R) Xeon(R) Gold 6338 CPU @ 2.00GHz | 2块 |
| 内存       |  Samsung, DRAM, 2933 MT/s, 64 GB        | 16条64GB内存条，共计1024GB      |
| GPU       | A100-SXM4-80GB | 8卡集群。每个训练/推理任务使用1卡      |
| NVIDIA Driver | 535.104.05 | NVIDIA-Linux-x86_64-535.104.05.run，需要管理员安装 |
| CUDA       | 12.2         | cuda_12.2.2_535.104.05_linux.run，需要管理员安装 |
| cudnn       | 8.9.2.26 | cudnn-linux-x86_64-8.9.2.26_cuda12-archive.tar.xz，需要管理员安装 |
| nccl  | 2.18.3 | nccl_2.18.3-1+cuda12.2_x86_64.txz，需要管理员安装 |

### 软件包版本依赖

其中，核心软件包版本：
| 软件包        | 版本号     | 备注   |
| :------------ | :-------   | :------- |
| python       | 3.10.14   | 本项目必需   |
| torch        | 2.3.0     | 本项目必需    |
| transformers | 4.40.2    | 本项目必需    |
| datasets     | 2.19.1    | 本项目必需    |
| accelerate   | 0.30.0    | 本项目必需    |
| peft         | 0.10.0    | 本项目必需    |
| trl          | 0.8.6     | 本项目无关，为RLHF时使用，本项目没有用到，但是llmtuner库需要依赖于这个 | 
| deepspeed    | 0.14.0    | 本项目必需 |
| bitsandbytes | 0.43.1    | 本项目必需 |
| flash-attn   | 2.5.8     | 本项目必需，可能需要手动单独运行```pip install flash-attn==2.5.8```，安装非常耗时，且可能存在不成功的可能，安装难度较大  |
| vllm         | 0.4.2     | 本项目必需，核心部署库，可能需要单独运行```pip install vllm==0.4.2```，安装非常耗时，且可能存在不成功的可能，安装难度较大，安装请参考：[https://docs.vllm.ai/en/latest/getting_started/installation.html](https://docs.vllm.ai/en/latest/getting_started/installation.html) |
| llmtuner     | 0.7.1.dev0 | **本项目必需，核心训练库，安装时可能需要用git clone的方式安装，参考[https://github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)**，安装时可以参考教程[https://zhuanlan.zhihu.com/p/695287607](https://zhuanlan.zhihu.com/p/695287607) |


### 调用大模型接口的环境变量依赖
本项目调用大模型（gpt-4-1106-preview、kimichat等）的部分依赖于[./data/BigFiveCPED/utils/MultiProcessingLLM](./data/BigFiveCPED/utils/MultiProcessingLLM)。
你可以从[https://platform.moonshot.cn](https://platform.moonshot.cn)、[https://api2d.com](https://api2d.com)当中注册账号申请api并使用LLM

本部分主要用于调用KimiChat API时用到。需要调用那些大模型，就设置那些API。
在使用前，需要配置环境变量，如下所示：
* 设置环境变量
```bash
vim ~/.bashrc
```
在其中增加以下语句并且保存

```bash
# 设置访问https://portal.azure.com提供的ChatGPT接口服务的api_key变量
# https://zhishenggpt.openai.azure.com/
export GPT35_AZURE_OPENAI_KEY='xxxx'
# https://zhishenggpt40.openai.azure.com/
export GPT4_AZURE_OPENAI_KEY='xxxx'

# https://openai.api2d.net/v1
export API2D_OPENAI_KEY='xxxx'

# https://dev.iai007.cloud/ai/api/v1
export HEFEI_OPENAI_KEY='xxxx'

# https://platform.moonshot.cn/console/api-keys
export KIMI_OPENAI_KEY='xxxx'
```
然后刷新环境配置
```bash
source ~/.bashrc
```


### 大模型参数下载(推荐)
建议使用[https://hf-mirror.com/](https://hf-mirror.com/)下载大模型，参考其中的**方法三：使用 hfd**，可以做到稳定下载不断线，示例如下：
* 设置环境变量
```bash
vim ~/.bashrc
```
在其中增加以下语句并且保存
```bash
export HF_ENDPOINT=https://hf-mirror.com
```
然后刷新环境配置
```bash
source ~/.bashrc
```

* 下载hfd工具

```bash
cd <你的保存大模型的路径>
wget https://hf-mirror.com/hfd/hfd.shchmod a+x hfd.sh
chmod a+x hfd.sh
```

* 运行下载命令
```bash
cd <你的保存大模型的路径>
./hfd.sh shenzhi-wang/Llama3-8B-Chinese-Chat --tool aria2c -x 4
./hfd.sh Qwen/Qwen1.5-14B-Chat --tool aria2c -x 4
```


## MedQA数据集
* 数据集来源：[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)
* 下载链接：[https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing)
* 中文介绍：[https://zhuanlan.zhihu.com/p/679590312](https://zhuanlan.zhihu.com/p/679590312)


## 数据集预处理

### 将txt文本转换为json文本(已完成，无需重复操作)
```bash
conda activate llama_factory
cd ./data/MedQA/utils

# txt转换为json
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/zh_paragraph' --output_json_dir '../data_clean/textbooks/zh_paragraph_json' --max_knowledge_len 1800 --language_type chinese --min_knowledge_len 5 --do_chunk
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/zh_sentence' --output_json_dir '../data_clean/textbooks/zh_sentence_json' --max_knowledge_len 1800 --language_type chinese --min_knowledge_len 5 --do_chunk
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/en' --output_json_dir '../data_clean/textbooks/en_json' --max_knowledge_len 1800 --language_type english --min_knowledge_len 5 --do_chunk
```

### 读取json文本完成向量化(已完成，无需重复操作)

```bash
# 根据json文件转换为向量
python -u vector_store.py --input_json_dir '../data_clean/textbooks/zh_sentence_json' --store_top_path '../data_clean/vector_stores/zh_sentence' 
python -u vector_store.py --input_json_dir '../data_clean/textbooks/zh_paragraph_json' --store_top_path '../data_clean/vector_stores/zh_paragraph'
python -u vector_store.py --input_json_dir '../data_clean/textbooks/en_json' --store_top_path '../data_clean/vector_stores/en'
```

### 执行训练集和测试集的检索，构建标准指令集(已完成，无需重复操作)

* 特别地，```--device_ids```参数指定使用的显卡，如果只有一张显卡，就设置```--device_ids="0"```,```--num_process=1```。
* 特别地，```--query_key_name```指定用于检索的query，可以选择"question"——仅用问题进行检索，或者"question_with_options"——问题与选项拼接在一起检索。最终方案使用了"question_with_options"。

* 特别地，需要先打开[./data/MedQA/utils/config.py](./data/MedQA/utils/config.py)修改"model_path"为服务器中检索Embedding模型的实际路径。


```bash
conda activate llama_factory
cd ./data/MedQA/utils

# 对json文件进行检索
# 中文数据集------检索仅使用"question"
# 训练集
python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/train.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/train" \
    --output_json_file="train.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"

# 验证集
python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/dev.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/dev" \
    --output_json_file="dev.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"

python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/test.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/test" \
    --output_json_file="test.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"


# 中文数据集------检索使用"question_with_options"
python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/train.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/train" \
    --output_json_file="train.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"

python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/dev.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/dev" \
    --output_json_file="dev.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"

python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/Mainland/test.jsonl" \
    --embedding_model_name="stella-base-zh-v2" \
    --store_path="../data_clean/vector_stores/zh_paragraph" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/test" \
    --output_json_file="test.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"


# 英文数据集------检索仅使用"question"
python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/train.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/train" \
    --output_json_file="train.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"

python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/dev.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/dev" \
    --output_json_file="dev.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"

python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/test.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/test" \
    --output_json_file="test.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question"


# 英文数据集------检索仅使用"question_with_options"
python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/train.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/train" \
    --output_json_file="train.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"



python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/dev.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/dev" \
    --output_json_file="dev.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"


python generate_question_with_knowledges.py \
    --num_process=8 \
    --index_key_name="id" \
    --topk_knowledge=10 \
    --knowledge_threshold=0.65 \
    --input_jsonl_path="../data_clean/questions/US/test.jsonl" \
    --embedding_model_name="stella-base-en-v2" \
    --store_path="../data_clean/vector_stores/en" \
    --output_json_dir="../data_clean/questions_with_knowledge/US/test" \
    --output_json_file="test.json" \
    --device_ids="0,1,2,3,4,5,6,7" \
    --query_key_name="question_with_options"
```


### 生成中文数据集的含有解析的文本(已完成，无需重复操作)

```bash
conda activate llama_factory
cd ./data/MedQA/utils

# 训练集
python ./MultiProcessingLLM/multiprocess_using_chatgpt_input_with_prompt_and_json_data.py --do_check \
    --num_process=30 \
    --model_name="moonshot-v1-32k_kimi" \
    --prompt_config_path="./MultiProcessingLLM/prompt_config_of_generate_explain.json" \
    --use_load_raw_json_data_with_process \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/train/retrive_use_question_with_options/stella-base-zh-v2/train.json" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/train/retrive_use_question_with_options/stella-base-zh-v2/train_with_explain_using_moonshot-v1-32k_kimi" \
    --list_placeholder="list_placeholder" \
    --llm_output_key="chatgpt_explain" \
    --index_key_name="id" \
    --temperature=0.7 \
    --max_tokens=4096 \
    --top_p=0.95

# 测试集
python ./MultiProcessingLLM/multiprocess_using_chatgpt_input_with_prompt_and_json_data.py --do_check \
    --num_process=30 \
    --model_name="moonshot-v1-32k_kimi" \
    --prompt_config_path="./MultiProcessingLLM/prompt_config_of_generate_explain.json" \
    --use_load_raw_json_data_with_process \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/test/retrive_use_question_with_options/stella-base-zh-v2/test.json" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/test/retrive_use_question_with_options/stella-base-zh-v2/test_with_explain_using_moonshot-v1-32k_kimi" \
    --list_placeholder="list_placeholder" \
    --llm_output_key="chatgpt_explain" \
    --index_key_name="id" \
    --temperature=0.7 \
    --max_tokens=4096 \
    --top_p=0.95


# 验证集
python ./MultiProcessingLLM/multiprocess_using_chatgpt_input_with_prompt_and_json_data.py --do_check \
    --num_process=30 \
    --model_name="moonshot-v1-32k_kimi" \
    --prompt_config_path="./MultiProcessingLLM/prompt_config_of_generate_explain.json" \
    --use_load_raw_json_data_with_process \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/dev/retrive_use_question_with_options/stella-base-zh-v2/dev.json" \
    --output_json_dir="../data_clean/questions_with_knowledge/Mainland/dev/retrive_use_question_with_options/stella-base-zh-v2/dev_with_explain_using_moonshot-v1-32k_kimi" \
    --list_placeholder="list_placeholder" \
    --llm_output_key="chatgpt_explain" \
    --index_key_name="id" \
    --temperature=0.7 \
    --max_tokens=4096 \
    --top_p=0.95
```

### 构建中文数据集的标准数据集(已完成，无需重复操作)
```bash
python format_json_dataset_for_training_llm.py \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/train/retrive_use_question_with_options/stella-base-zh-v2/train_with_explain_using_moonshot-v1-32k_kimi" \
    --dataset_info_path=""../../dataset_info.json \
    --dataset_name="RAG_MedQA_Mainland_train" \
    --dataset_info_relative_dir="MedQA/" \
    --output_json_data_dir="../" \
    --do_register_dataset

# 构建测试集
python format_json_dataset_for_training_llm.py \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/test/retrive_use_question_with_options/stella-base-zh-v2/test_with_explain_using_moonshot-v1-32k_kimi" \
    --dataset_info_path=""../../dataset_info.json \
    --dataset_name="RAG_MedQA_Mainland_test" \
    --dataset_info_relative_dir="MedQA/" \
    --output_json_data_dir="../" \
    --do_register_dataset
```

2. Jamba 模型推理微调操作说明

一、概述
本说明详细涵盖了 Jamba 模型的 large 和 mini 版本的推理操作，以及 Jamba mini 版本的微调（finetune）和微调后的推理使用方法，为相关操作提供全面指导。

二、环境准备
（一）依赖库安装

### 曙光云容器配置

其中硬件与驱动依赖：

jamba mini (推理和微调)
16 核心; 120.0G 内存; 2 加速器 | 单实例

jamba large
64 核心; 480.0G 内存; 8 加速器 | 单实例

### 软件包版本依赖
 曙光云镜像名称(推理和微调)
 __jupyterlab-pytorch_0707:2.2.0-py3.10-cuda12.1-ubuntu22.04-devel_0707__

镜像包中已包含conda环境
```bash
conda activate jamba
```

（二）路径说明
源码目录：/work/home/acbjfbaxkm/Jamba-Test

该目录下包含以下关键文件：
```bash
jamba16large_inference.py
jamba16mini_finetune.py
jamba16mini_inference.py
jamba16mini_inference_by_finetune.py
```

Jamba 模型主路径：/work/home/acbjfbaxkm/AI21Labs

此目录下包含：

```bash
AI21-Jamba-Mini-1.6
AI21-Jamba-Large-1.6
带有 <_nept_k4>、<_nept_k6>、<_nept_k....> 等后缀的目录，这些目录是通过修改 config.json 中第 26 行 num_experts_per_tok 对应的值（原值为 2）得到的。
```


__数据集主路径：/work/home/acbjfbaxkm/DataSet (以下数据集已通过上述操作进行处理,无需重复执行)
该目录下包含：
__USMLE 目录
```bash
RAG_MedQA_USS_test_train.json：训练数据集（354 条）
MedQA_USS_test.json：不包含知识的数据集（354 条）
RAG_MedQA_USS_test.json：包含知识的数据集（354 条）
```
__MCQA 目录
```bash
Med_MCQA_knowledge_test_train.json：训练数据集（300 条）
Med_MCQA_test.json：不包含知识的数据集（300 条）
Med_MCQA_knowledge_test.json：包含知识的数据集（300 条）
```


三、Jamba 16 Large 版本推理
（一）代码文件
```bash
jamba16large_inference.py
```
（二）执行步骤
设置参数：确保代码中的 fixed_path、dataset_path、temperature、top_k、top_p 等参数设置正确。
执行命令：
```bash
python jamba16large_inference.py <model_name> <dataset_filenames>
```

（三）参数说明
<model_name>：模型名称，例如 AI21-Jamba-Large-16。
<dataset_filenames>：数据集文件名，可以传入多个文件名，用空格分隔，例如 dataset1.json dataset2.json。
（四）示例
```bash
python jamba16large_inference.py AI21-Jamba-Large-1.6 USMLE/MedQA_USS_test.json
```

四、Jamba 16 Mini 版本推理
（一）代码文件
jamba16mini_inference.py
（二）执行步骤
设置参数：确保代码中的 fixed_path、dataset_path、temperature、top_k、top_p 等参数设置正确。
执行命令：
```bash
python jamba16mini_inference.py <model_name> <dataset_filenames>
```

（三）参数说明
<model_name>：模型名称，例如 AI21-Jamba-Mini-1.6。
<dataset_filenames>：数据集文件名，可以传入多个文件名，用空格分隔，例如 dataset1.json dataset2.json。
（四）示例
```bash
python jamba16mini_inference.py AI21-Jamba-Mini-1.6 USMLE/MedQA_USS_test.json
```

五、Jamba 16 Mini 版本 Finetune
（一）代码文件
jamba16mini_finetune.py
（二）执行步骤
设置参数：可以通过命令行参数设置模型名称和数据集路径。
执行命令：
```bash
python jamba16mini_finetune.py <model_name> <dataset_path>
```

（三）参数说明
<model_name>：模型名称，例如 AI21-Jamba-Mini-1.6。
<dataset_path>：数据集路径，例如 RAG_MedQA_USS_test_train.json。
（四）示例
```bash
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 RAG_MedQA_USS_test_train.json
```

（五）finetune 结果
保存目录为 /work/home/acbjfbaxkm/Jamba-Test/finetune_result。
六、Jamba 16 Mini 版本 Finetune 后的推理
（一）代码文件
```bash
jamba16mini_inference_by_finetune.py
```
（二）执行步骤
设置参数：确保代码中的 fixed_path、dataset_path、temperature、top_k、top_p、peft_fixed_path 等参数设置正确。
执行命令：
```bash
python jamba16mini_inference_by_finetune.py <model_name> <dataset_filenames> <peft_relative_path>
```

（三）参数说明
<model_name>：模型名称，例如 AI21-Jamba-Mini-1.6。
<dataset_filenames>：数据集文件名，可以传入多个文件名，用空格分隔，例如 dataset1.json dataset2.json。
<peft_relative_path>：Peft 模型的相对路径，固定路径为 /work/home/acbjfbaxkm/Jamba-Test/finetune_result，只需输入相对路径，例如 AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300。
（四）示例
```bash
python jamba16mini_inference_by_finetune.py AI21-Jamba-Mini-1.6 MCQA/Med_MCQA_knowledge_test AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300
```

（五）说明
推理前代码中会将原模型（例如 AI21-Jamba-Mini-1.6）跟 finetune 后的 lora 权重合并至 peft_relative_path 路径下的 merged 目录。

七、结果保存
推理结果将保存到 /work/home/acbjfbaxkm/Jamba-Test/results 目录下，文件名格式为：
```bash
jamba16<版本>_inference_<相关信息>_temperature<温度值>_topp<top_p值>_topk<top_k值>_<时间戳>.xlsx
```

八、推理提取答案说明
推理代码中都有一个提取模型回复答案的函数 <extract_predicted_option_by_us>。
如遇见新的模型输出答案格式，可以在函数 <extract_predicted_option_by_us> 中加入对应表达式。
```bash
extract_answer.py 
```
用于重新处理提取结果文件（.xlsx）的模型回复的答案。
使用示例：
```bash
python extract_answer.py --directory /path/to/your/directory
```

以上说明中的参数和路径请根据实际情况进行调整。

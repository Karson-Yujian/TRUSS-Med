# TRUSS-Med: Medical Question Answering via Transformers, Retrieval, and Unified State Space Models

Jamba Model Debugging Guide

> This document follows the original operating guide. The `data/` directory is reused from the [reference project's data directory](https://github.com/julienamaury/Medical-Answering-Model-202410/tree/2ce178140e0aab1cbe56691f28bbee00c3f09294/data) and contains the MedQA data, data-processing code, and `dataset_info.json`. Only cache files and directories such as `.DS_Store`, `__pycache__`, and `.ipynb_checkpoints` were excluded during copying. `data/MCQA/` is currently empty and will be populated later. Part 2 describes the Jamba procedures used in this project.

# 1. Dataset Construction

## Project Environment and Dependencies

The project primarily uses the following conda environment on Alibaba Cloud:
```bash
conda activate llama_factory
```
See [requirements.txt](requirements.txt) for the complete dependency list and versions. The following version table records the original dataset-construction environment, which differs from the Jamba environment described in Part 2.

### Hardware and System-Level Driver Requirements

The hardware and driver requirements are as follows:
| Software/Hardware        | Version/Configuration     | Notes   |
| ------------ | -------    | ------- |
| Operating system       | Ubuntu 20.04.1 LTS |    |
| CPU       | Intel(R) Xeon(R) Gold 6338 CPU @ 2.00GHz | 2 CPUs |
| Memory       |  Samsung, DRAM, 2933 MT/s, 64 GB        | 16 × 64 GB modules, 1,024 GB total      |
| GPU       | A100-SXM4-80GB | 8-GPU cluster; each training/inference task uses 1 GPU      |
| NVIDIA Driver | 535.104.05 | NVIDIA-Linux-x86_64-535.104.05.run; administrator installation required |
| CUDA       | 12.2         | cuda_12.2.2_535.104.05_linux.run; administrator installation required |
| cuDNN       | 8.9.2.26 | cudnn-linux-x86_64-8.9.2.26_cuda12-archive.tar.xz; administrator installation required |
| NCCL  | 2.18.3 | nccl_2.18.3-1+cuda12.2_x86_64.txz; administrator installation required |

### Package Version Requirements

The core package versions are as follows:
| Package        | Version     | Notes   |
| :------------ | :-------   | :------- |
| Python       | 3.10.14   | Required by this project   |
| PyTorch        | 2.3.0     | Required by this project    |
| Transformers | 4.40.2    | Required by this project    |
| Datasets     | 2.19.1    | Required by this project    |
| Accelerate   | 0.30.0    | Required by this project    |
| PEFT         | 0.10.0    | Required by this project    |
| TRL          | 0.8.6     | Used for RLHF and not directly used in this project, but required by the llmtuner library |
| DeepSpeed    | 0.14.0    | Required by this project |
| bitsandbytes | 0.43.1    | Required by this project |
| FlashAttention   | 2.5.8     | Required by this project. You may need to run ```pip install flash-attn==2.5.8``` separately. Installation is time-consuming, may fail, and can be difficult.  |
| vLLM         | 0.4.2     | Required by this project and used as the core deployment library. You may need to run ```pip install vllm==0.4.2``` separately. Installation is time-consuming, may fail, and can be difficult. See the [vLLM installation guide](https://docs.vllm.ai/en/latest/getting_started/installation.html). |
| llmtuner     | 0.7.1.dev0 | **Required by this project and used as the core training library. Installation may require cloning the [LLaMA-Factory repository](https://github.com/hiyouga/LLaMA-Factory) with Git.** You may also consult this [installation tutorial](https://zhuanlan.zhihu.com/p/695287607). |


### Environment Variables for Large Language Model APIs
The components that call large language models such as gpt-4-1106-preview and KimiChat depend on [data/MedQA/utils/MultiProcessingLLM](data/MedQA/utils/MultiProcessingLLM).
You can register with [Moonshot AI](https://platform.moonshot.cn) or [API2D](https://api2d.com), request an API credential, and use the corresponding LLM service.

This section primarily applies when calling the KimiChat API. Configure the API credentials for the large language models you intend to use.
Before use, configure the environment variables as follows:
* Configure environment variables
```bash
vim ~/.bashrc
```
Add the following lines and save the file:

```bash
# Set the api_key variables for the ChatGPT services provided through https://portal.azure.com
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
Then reload the environment configuration:
```bash
source ~/.bashrc
```


### Downloading Large Language Model Weights (Recommended)
We recommend downloading large language models from [https://hf-mirror.com/](https://hf-mirror.com/). Follow **Method 3: Use hfd** for stable, resumable downloads. An example is provided below:
* Configure the environment variable
```bash
vim ~/.bashrc
```
Add the following line and save the file:
```bash
export HF_ENDPOINT=https://hf-mirror.com
```
Then reload the environment configuration:
```bash
source ~/.bashrc
```

* Download the hfd tool

```bash
cd <path_to_your_model_storage_directory>
wget https://hf-mirror.com/hfd/hfd.sh
chmod a+x hfd.sh
```

* Run the download commands
```bash
cd <path_to_your_model_storage_directory>
./hfd.sh shenzhi-wang/Llama3-8B-Chinese-Chat --tool aria2c -x 4
./hfd.sh Qwen/Qwen1.5-14B-Chat --tool aria2c -x 4
```


## MedQA Dataset
* Dataset source: [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)
* Download link: [https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing)
* Chinese introduction: [https://zhuanlan.zhihu.com/p/679590312](https://zhuanlan.zhihu.com/p/679590312)


### MedMCQA Dataset

* Dataset source: [MedMCQA](https://github.com/medmcqa/medmcqa)
* Download link: [Official dataset download](https://drive.google.com/uc?export=download&id=15VkJdq5eyWIkfb_aoD3oS8i4tScbHYky)

## Dataset Preprocessing

“Completed” means that the step was completed in the original experiment. This repository includes the raw data, processing code, and example outputs required by the following steps. To rebuild the dataset, run the original procedure below from the project root.

### Convert TXT Files to JSON (Completed; No Need to Repeat)
```bash
conda activate llama_factory
cd ./data/MedQA/utils

# Convert TXT files to JSON
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/zh_paragraph' --output_json_dir '../data_clean/textbooks/zh_paragraph_json' --max_knowledge_len 1800 --language_type chinese --min_knowledge_len 5 --do_chunk
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/zh_sentence' --output_json_dir '../data_clean/textbooks/zh_sentence_json' --max_knowledge_len 1800 --language_type chinese --min_knowledge_len 5 --do_chunk
python -u txt2json.py --input_txt_dir '../data_clean/textbooks/en' --output_json_dir '../data_clean/textbooks/en_json' --max_knowledge_len 1800 --language_type english --min_knowledge_len 5 --do_chunk
```

### Read and Vectorize JSON Files (Completed; No Need to Repeat)

```bash
# Convert JSON files into vectors
python -u vector_store.py --input_json_dir '../data_clean/textbooks/zh_sentence_json' --store_top_path '../data_clean/vector_stores/zh_sentence'
python -u vector_store.py --input_json_dir '../data_clean/textbooks/zh_paragraph_json' --store_top_path '../data_clean/vector_stores/zh_paragraph'
python -u vector_store.py --input_json_dir '../data_clean/textbooks/en_json' --store_top_path '../data_clean/vector_stores/en'
```

### Retrieve Knowledge for the Training and Test Sets and Build the Standard Instruction Dataset (Completed; No Need to Repeat)

* The ```--device_ids``` parameter specifies the GPUs to use. If only one GPU is available, set ```--device_ids="0"``` and ```--num_process=1```.
* The ```--query_key_name``` parameter specifies the retrieval query. Use `"question"` to retrieve with the question alone, or `"question_with_options"` to retrieve with the question and answer options concatenated. The final configuration uses `"question_with_options"`.

* Before running retrieval, open [data/MedQA/utils/config.py](data/MedQA/utils/config.py) and set `"model_path"` to the actual path of the retrieval embedding model on the server.


```bash
conda activate llama_factory
cd ./data/MedQA/utils

# Retrieve knowledge for JSON files
# Chinese dataset—retrieve using "question" only
# Training set
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

# Validation set
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


# Chinese dataset—retrieve using "question_with_options"
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


# English dataset—retrieve using "question" only
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


# English dataset—retrieve using "question_with_options" only
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


### Generate Chinese Dataset Text with Explanations (Completed; No Need to Repeat)

```bash
conda activate llama_factory
cd ./data/MedQA/utils

# Training set
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

# Test set
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


# Validation set
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

### Build the Standard Chinese Dataset (Completed; No Need to Repeat)
```bash
python format_json_dataset_for_training_llm.py \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/train/retrive_use_question_with_options/stella-base-zh-v2/train_with_explain_using_moonshot-v1-32k_kimi" \
    --dataset_info_path="../../dataset_info.json" \
    --dataset_name="RAG_MedQA_Mainland_train" \
    --dataset_info_relative_dir="MedQA/" \
    --output_json_data_dir="../" \
    --do_register_dataset

# Build the test set
python format_json_dataset_for_training_llm.py \
    --input_json_data_path="../data_clean/questions_with_knowledge/Mainland/test/retrive_use_question_with_options/stella-base-zh-v2/test_with_explain_using_moonshot-v1-32k_kimi" \
    --dataset_info_path="../../dataset_info.json" \
    --dataset_name="RAG_MedQA_Mainland_test" \
    --dataset_info_relative_dir="MedQA/" \
    --output_json_data_dir="../" \
    --do_register_dataset
```

# 2. Jamba Model Inference and Fine-Tuning Guide

## I. Overview

This guide covers inference with the large and mini versions of the Jamba model, fine-tuning of Jamba mini, and inference with a fine-tuned Jamba mini model, providing comprehensive guidance for each procedure.

## II. Environment Setup

(1) Dependency Installation

### Sugon Cloud Container Configuration

The hardware and driver requirements are as follows:

jamba mini (inference and fine-tuning)
16 cores; 120.0 GB memory; 2 accelerators | single instance

jamba large
64 cores; 480.0 GB memory; 8 accelerators | single instance

### Package Version Requirements
 Sugon Cloud image name (inference and fine-tuning)
 __jupyterlab-pytorch_0707:2.2.0-py3.10-cuda12.1-ubuntu22.04-devel_0707__

The image already includes the conda environment:
```bash
conda activate jamba
```

(2) Path Reference
Original server source directory: /work/home/acbjfbaxkm/Jamba-Test

The repository's four model scripts are located in `jamba/`. Enter this directory and create the results directory before running the commands below:

```bash
cd /path/to/TRUSS-Med/jamba
mkdir -p results
```

The fixed paths for the models, datasets, and fine-tuning outputs remain configured as in the original scripts. Adjust them to match your deployment location.

This directory contains the following key files:
```bash
jamba16large_inference.py
jamba16mini_finetune.py
jamba16mini_inference.py
jamba16mini_inference_by_finetune.py
```

Jamba model root path: /work/home/acbjfbaxkm/AI21Labs

This directory contains:

```bash
AI21-Jamba-Mini-1.6
AI21-Jamba-Large-1.6
Directories with suffixes such as <_nept_k4>, <_nept_k6>, and <_nept_k....>. These directories were produced by changing the value of `num_experts_per_tok` on line 26 of `config.json` from its original value of 2.
```


The dataset root path used in the original experiment was `/work/home/acbjfbaxkm/DataSet`. This repository can directly use the copied data under `data/MedQA`; an absolute path to the dataset file can be passed when running a script.
The directory contains:
**MedQA Directory**
```bash
data/MedQA/RAG_MedQA_Mainland_train_500(example).json: training examples containing messages and answer_idx
data/MedQA/data_clean/questions: raw MedQA question data
data/MedQA/data_clean/textbooks: raw medical textbook text and converted JSON data
```
**MCQA Directory**
```bash
data/MCQA/: currently empty and located at the same level as data/MedQA/; MedMCQA data will be added later
```


## III. Jamba 16 Large Inference

(1) Code File
```bash
jamba16large_inference.py
```
(2) Procedure
Configure the parameters: ensure that `fixed_path`, `dataset_path`, `temperature`, `top_k`, `top_p`, and other parameters in the code are set correctly.
Run the command:
```bash
python jamba16large_inference.py <model_name> <dataset_filenames>
```

(3) Parameter Descriptions
`<model_name>`: model name, for example, AI21-Jamba-Large-1.6.
`<dataset_filenames>`: dataset filenames. Multiple filenames can be supplied and separated by spaces, for example, dataset1.json dataset2.json.
(4) Example
```bash
python jamba16large_inference.py AI21-Jamba-Large-1.6 "$(cd .. && pwd)/data/MedQA/RAG_MedQA_Mainland_train_500(example).json"
```

## IV. Jamba 16 Mini Inference

(1) Code File
jamba16mini_inference.py
(2) Procedure
Configure the parameters: ensure that `fixed_path`, `dataset_path`, `temperature`, `top_k`, `top_p`, and other parameters in the code are set correctly.
Run the command:
```bash
python jamba16mini_inference.py <model_name> <dataset_filenames>
```

(3) Parameter Descriptions
`<model_name>`: model name, for example, AI21-Jamba-Mini-1.6.
`<dataset_filenames>`: dataset filenames. Multiple filenames can be supplied and separated by spaces, for example, dataset1.json dataset2.json.
(4) Example
```bash
python jamba16mini_inference.py AI21-Jamba-Mini-1.6 "$(cd .. && pwd)/data/MedQA/RAG_MedQA_Mainland_train_500(example).json"
```

## V. Jamba 16 Mini Fine-Tuning

(1) Code File
jamba16mini_finetune.py
(2) Procedure
Configure the parameters: set the model name and dataset path through the command-line arguments.
Run the command:
```bash
python jamba16mini_finetune.py <model_name> <dataset_path>
```

(3) Parameter Descriptions
`<model_name>`: model name, for example, AI21-Jamba-Mini-1.6.
`<dataset_path>`: dataset path, for example, RAG_MedQA_USS_test_train.json.
(4) Example
```bash
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 "$(cd .. && pwd)/data/MedQA/RAG_MedQA_Mainland_train_500(example).json"
```

(5) Fine-Tuning Results
Results are saved to `/work/home/acbjfbaxkm/Jamba-Test/finetune_result`.
## VI. Inference with a Fine-Tuned Jamba 16 Mini Model

(1) Code File
```bash
jamba16mini_inference_by_finetune.py
```
(2) Procedure
Configure the parameters: ensure that `fixed_path`, `dataset_path`, `temperature`, `top_k`, `top_p`, `peft_fixed_path`, and other parameters in the code are set correctly.
Run the command:
```bash
python jamba16mini_inference_by_finetune.py <model_name> <dataset_filenames> <peft_relative_path>
```

(3) Parameter Descriptions
`<model_name>`: model name, for example, AI21-Jamba-Mini-1.6.
`<dataset_filenames>`: dataset filenames. Multiple filenames can be supplied and separated by spaces, for example, dataset1.json dataset2.json.
`<peft_relative_path>`: relative path to the PEFT model. The fixed root path is `/work/home/acbjfbaxkm/Jamba-Test/finetune_result`, so only the relative path is required, for example, AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300.
(4) Example
```bash
python jamba16mini_inference_by_finetune.py AI21-Jamba-Mini-1.6 "$(cd .. && pwd)/data/MedQA/RAG_MedQA_Mainland_train_500(example).json" "AI21-Jamba-Mini-1.6/RAG_MedQA_Mainland_train_500(example)/checkpoint-300"
```

(5) Notes
Before inference, the code merges the original model, such as AI21-Jamba-Mini-1.6, with the fine-tuned LoRA weights into the `merged` directory under `peft_relative_path`.

## VII. Saving Results

Inference results are saved to `results/` under the current working directory. When the commands above are followed, the directory is `jamba/results/`. The filename format is:
```bash
jamba16<version>_inference_<related_information>_temperature<temperature_value>_topp<top_p_value>_topk<top_k_value>_<timestamp>.xlsx
```

## VIII. Extracting Answers from Inference Results

Each inference script contains an `<extract_predicted_option_by_us>` function that extracts the answer from the model response.
If a new model output format is encountered, add the corresponding expression to `<extract_predicted_option_by_us>`.
```bash
extract_answer.py
```
This script reprocesses and extracts answers from model responses in result files (`.xlsx`). The original script overwrites the corresponding result files.
Example:
```bash
cd ../utils
python extract_answer.py --directory /path/to/your/directory
```

Adjust the parameters and paths in this guide to match the actual environment.

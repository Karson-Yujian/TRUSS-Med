# ZhiyiChat (MedQA)

[English](README.md) | 简体中文

基于 Jamba 1.6 的医学选择题实验，支持 MedQA、MedMCQA 的推理、Mini LoRA 微调、微调后推理和结果评估。

**本次仅发布代码与文档，不上传 `MedQA/`、`MedMCQA/` 两个数据集目录。** 下文的数据目录和文件表描述本地实验布局；从 GitHub 获取代码后，需自行准备数据。

本文以[线上参考 README](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/README_zh.md)的章节顺序和数据处理流程为标准，保留本项目原有 Jamba 文件名、参数和执行逻辑。线上项目使用 LLaMA-Factory，本项目使用独立 Jamba 脚本；两者的训练入口和环境版本不能直接混用。核对日期：2026-10-08，详见[逐项核对记录](readme/线上核对说明.md)。

## 项目环境依赖

优先使用原来已运行成功的 Jamba Linux/CUDA 环境。当前 `requirements.txt` 是依赖名称清单，尚不是验证过的版本锁定文件。

```bash
pip install -r requirements.txt
```

### 硬件与系统级驱动依赖

原项目中文说明记载：Mini 环境为 16 核、120 GB 内存、2 个加速器；Large 为 64 核、480 GB 内存、8 个加速器。它们是历史配置，不是经本次验证的最低需求。运行前检查 GPU 型号、显存、驱动、CUDA 以及脚本中的 `number_gpus`。

线上 README 的硬件表对应其自己的实验环境，不能直接作为 Jamba 的硬件保证。本项目尚未补齐目标服务器的实际驱动与显存记录。

### 软件包版本依赖

原 Jamba 微调脚本调用 `trl.SFTConfig(max_seq_length=...)` 和 `SFTTrainer`，需要兼容这些接口的版本。线上表格中的 LLaMA-Factory 及旧版依赖组合仅供核对，不作为本项目安装锁定版本。部署成功后应记录 Python、PyTorch、Transformers、TRL、PEFT、vLLM、CUDA 版本。

### 调用大模型接口的环境变量依赖

Jamba 本地推理与微调不调用外部模型 API。下文“生成解析”步骤才涉及 API 服务及环境变量；对应实现尚未迁入当前项目，故不添加无实际消费者的密钥配置。原项目 `dataset_handle/` 中可找到相关调用实现，详见核对记录。

### 大模型参数下载

下载对应的 [Jamba Mini 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Mini-1.6) 或 [Jamba Large 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6)，保留完整配置、tokenizer 和权重文件。下载及访问要求以模型页面为准。

原脚本通过 `fixed_path` 与模型目录名拼接定位模型；微调脚本则在 `main()` 中直接指定根路径。请按原方式修改部署路径。默认模型根路径为 `/work/home/acbjfbaxkm/AI21Labs`。知识检索还需要独立的 embedding 模型，不能用 Jamba 路径替代。

## MedQA 数据集

- 来源：[MedQA 官方仓库](https://github.com/jind11/MedQA)。
- 下载：[题目与教材](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing)。
- 论文：[What Disease does this Patient Have?](https://arxiv.org/abs/2009.13081)。
- 本地原始题目和教材：`MedQA/data_clean/`；已处理的实验输入：`MedQA/result/`。

### MedMCQA 数据集

- 来源：[MedMCQA 官方仓库](https://github.com/medmcqa/medmcqa)与[项目主页](https://medmcqa.github.io/)。
- 下载：[官方数据下载](https://drive.google.com/uc?export=download&id=15VkJdq5eyWIkfb_aoD3oS8i4tScbHYky)。
- 论文：[MedMCQA](https://proceedings.mlr.press/v174/pal22a.html)。
- 本地原始数据：`MedMCQA/data/`；处理后数据：`MedMCQA/result/`。MedMCQA 是本项目在参考 MedQA 流程基础上保留的数据集分支。

### 本项目使用的实验文件

| 用途 | MedQA（每文件 354 条） | MedMCQA（每文件 300 条） |
| --- | --- | --- |
| 普通推理 | `MedQA/result/MedQA_USS_test.json` | `MedMCQA/result/Med_MCQA_test.json` |
| 含知识推理 | `MedQA/result/RAG_MedQA_USS_test.json` | `MedMCQA/result/Med_MCQA_knowledge_test.json` |
| 微调 | `MedQA/result/RAG_MedQA_USS_test_train.json` | `MedMCQA/result/Med_MCQA_knowledge_test_train.json` |

这些是本地处理后的实验文件，不是官方完整划分。原始 MedQA JSONL、原始 MedMCQA 选项字段不能直接代替 Jamba 所需的 `messages` JSON 数组。推理记录还需 `answer_idx` 用于比较答案。历史训练文件名不保证与测试集互斥，抽样与划分依据仍需补充。

## 数据集预处理

保留线上五个步骤及先后关系：教材分块 → 向量库 → 问题检索 → 解析生成 → 训练/测试格式转换。原中文说明已记录此过程；**流程说明存在不等于当前项目包含所有实现**。以下按线上源码定位列出状态，不把缺失脚本标成可直接运行。

### 将 txt 文本转换为 JSON 文本

输入为中英文教材，输出为分块后的 JSON 文本。线上入口是 [`txt2json.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/txt2json.py)。本项目和原项目均未找到同名脚本；保留此步骤，待迁入对应实现后才能从教材重新构建。

### 读取 JSON 文本完成向量化

分块文本经 embedding 编码后建立检索库。线上入口是 [`vector_store.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/vector_store.py)。本地未找到同名实现或向量索引；原项目仅保留部分 `embedding.py`、`config.py` 支持代码。

### 执行训练集和测试集的检索，构建标准指令集

线上入口是 [`generate_question_with_knowledges.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/generate_question_with_knowledges.py)，按问题或问题加选项检索知识；依赖 `retriever.py` 和 embedding 配置。

原项目有 `dataset_handle/generate_question_with_knowledges_mcqa.py`、`generate_mcqa_question_with_knowledges.py` 两个变体，但导入的 `retriever.py` 本地缺失。当前新项目未迁入这些脚本；已有含知识数据可以用于后续 Jamba 实验。

### 生成中文数据集的含有解析的文本

此步以检索结果为输入，通过外部模型及提示词生成解析。线上实现位于 [`MultiProcessingLLM/`](https://github.com/julienamaury/Medical-Answering-Model-202410/tree/main/data/MedQA/utils/MultiProcessingLLM)。原项目 `dataset_handle/` 有批量调用脚本、API 封装和英文提示词配置，当前尚未迁入；不能将其视为已完整移植的中文解析生成环境。

### 构建中文数据集的标准数据集

线上入口是 [`format_json_dataset_for_training_llm.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/format_json_dataset_for_training_llm.py)，将题目、知识和解析转换为对话数据。原项目有同名文件和 MCQA 变体，当前未迁入。

线上额外注册 `dataset_info.json` 供 LLaMA-Factory 使用；本项目的 Jamba 脚本直接读取 JSON 文件，不需要为运行现有脚本引入该注册机制。训练文件包含 assistant 目标；原 Jamba 推理脚本在构造提示时过滤 assistant 消息。

各阶段的完整历史参数仍保存在[原中文操作说明](readme/Jamba模型操作说明.md)中。原文件内容未改，历史路径不代表当前新项目中已具备相应实现。

## 微调与测试

继续按原文件名执行。下面用绝对数据路径，避免线上 `data/MedQA/`、历史服务器 `USMLE/MCQA/` 与本仓库目录混淆。原代码的 `os.path.join` 支持这些绝对路径，无需修改处理逻辑。

```bash
PROJECT='/path/to/ZhiyiChat(MedQA)'
cd "$PROJECT/jamba"
mkdir -p results
```

模型路径及 GPU/采样参数仍在各脚本中配置；微调输出根路径在 `jamba16mini_finetune.py` 内设置，微调后推理使用 `peft_fixed_path`。它们默认指向原服务器位置，部署时须对应修改。

### 微调

```bash
# MedQA
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedQA/result/RAG_MedQA_USS_test_train.json"
# MedMCQA
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test_train.json"
```

两个参数依次为模型目录名和数据路径。保留原 LoRA 参数、SFTTrainer 与保存逻辑。适配器输出位于配置的 `finetune_result/<model_name>/<dataset_name>/`，实际 checkpoint 名以训练结果为准。

### 测试

```bash
# Mini 普通推理：MedQA + MedMCQA
python jamba16mini_inference.py AI21-Jamba-Mini-1.6 "$PROJECT/MedQA/result/MedQA_USS_test.json" "$PROJECT/MedMCQA/result/Med_MCQA_test.json"
# Large 含知识推理：MedQA + MedMCQA
python jamba16large_inference.py AI21-Jamba-Large-1.6 "$PROJECT/MedQA/result/RAG_MedQA_USS_test.json" "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test.json"
# Mini 微调后推理，最后参数替换为实际 adapter 目录
python jamba16mini_inference_by_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test.json" /path/to/actual-adapter
```

普通与含知识数据都可交给 Mini 或 Large 脚本；以上只是示例组合。微调后脚本在 adapter 目录内合并为 `merged/`，随后在同一进程中推理。输出 Excel 位于当前工作目录的 `results/`。

### 测试结果标准化与统计准确率

推理脚本直接输出逐题 Excel 并计算准确率，因此不需要照搬线上 LLaMA-Factory 的 JSONL 转 Excel 入口。需要重新提取答案时：

```bash
cd "$PROJECT/utils"
python extract_answer.py --directory "$PROJECT/jamba/results"
```

该脚本按原正则重新处理答案并覆盖原结果表。保留原有评估逻辑，未更改分母、匹配规则或异常处理。

### 批量测试

现有推理脚本支持一次传入多个数据文件，示例见“测试”。线上还有温度、top-p、checkpoint 多组合调度和跨实验成绩汇总；当前 Jamba 项目尚无对应调度或汇总脚本。多数据集输入不能等同于完整参数扫描。

## 项目文件与发布准备

```text
jamba/       四个原始 Jamba 1.6 脚本
utils/       extract_answer.py
MedQA/       原始题目、教材和 result/ 实验输入
MedMCQA/     原始数据与 result/ 实验输入
readme/      原始双语说明、线上核对记录
```

两个重复/参数错误的旧 MCQA 推理脚本及 v0.1 训练脚本已从新项目移除；四个 Jamba 核心脚本保持原样。没有引入统一 CLI 或 workflow。

本次代码发布通过 `.gitignore` 排除 `MedQA/`、`MedMCQA/`，本地数据仍保留。数据没有纳入当前提交历史，本次不需要上传 Git LFS 对象。

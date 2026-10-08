# ZhiyiChat (MedQA)

English | [简体中文](README_zh.md)

Jamba 1.6 medical multiple-choice experiments: MedQA/MedMCQA inference, Mini LoRA training, post-training inference and evaluation.

**This release contains code and documentation only; `MedQA/` and `MedMCQA/` are not uploaded.** Dataset paths below describe the local experiment layout. Prepare the data separately after cloning.

This guide follows the section order and data-processing stages of the [online reference README](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/README_zh.md), while preserving this project's original Jamba filenames, arguments and implementation. The reference uses LLaMA-Factory; its training commands and dependency versions are not interchangeable with these standalone scripts. Checked on 2026-10-08; see the [file-level comparison](readme/线上核对说明.md).

## Project environment dependencies

Prefer the original working Linux/CUDA Jamba environment. `requirements.txt` lists dependency names, not a validated lockfile.

```bash
pip install -r requirements.txt
```

### Hardware and system drivers

The original local guide records 16 CPU cores, 120 GB RAM and two accelerators for Mini; 64 cores, 480 GB RAM and eight accelerators for Large. These are historical configurations, not verified minimum requirements. Check GPU model, VRAM, driver, CUDA and `number_gpus` before running. The online project's hardware table describes its own experiments, not a Jamba guarantee. Target-server driver and VRAM records remain to be supplied.

### Package versions

The existing training script requires TRL interfaces supporting `SFTConfig(max_seq_length=...)` and its `SFTTrainer` call. Do not copy the online LLaMA-Factory dependency table as a Jamba lockfile. Record Python, PyTorch, Transformers, TRL, PEFT, vLLM and CUDA versions after a successful server run.

### External model API environment variables

Local Jamba training/inference does not call hosted model APIs. Only the explanation-generation stage below needs API credentials. That implementation is not currently migrated; therefore this guide does not introduce unused credential settings. Related wrappers exist in the original project's `dataset_handle/` directory.

### Downloading model weights

Obtain [Jamba Mini 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Mini-1.6) or [Jamba Large 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6), retaining complete configuration, tokenizer and weight files. Follow the model pages for download/access requirements.

Inference resolves the model directory under `fixed_path`; training constructs paths inside `main()`. Edit these locations using the original configuration method. The historical model root is `/work/home/acbjfbaxkm/AI21Labs`. Knowledge retrieval requires a separate embedding model.

## MedQA dataset

- [Official repository](https://github.com/jind11/MedQA), [questions and textbooks](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing), [paper](https://arxiv.org/abs/2009.13081).
- Original questions/textbooks: `MedQA/data_clean/`; prepared experiment inputs: `MedQA/result/`.

### MedMCQA dataset

- [Official repository](https://github.com/medmcqa/medmcqa), [homepage](https://medmcqa.github.io/), [download](https://drive.google.com/uc?export=download&id=15VkJdq5eyWIkfb_aoD3oS8i4tScbHYky), [paper](https://proceedings.mlr.press/v174/pal22a.html).
- Original data: `MedMCQA/data/`; prepared inputs: `MedMCQA/result/`. This is the additional dataset branch retained by this project.

### Prepared experiment files

| Purpose | MedQA (354 records/file) | MedMCQA (300 records/file) |
| --- | --- | --- |
| Plain inference | `MedQA/result/MedQA_USS_test.json` | `MedMCQA/result/Med_MCQA_test.json` |
| Knowledge inference | `MedQA/result/RAG_MedQA_USS_test.json` | `MedMCQA/result/Med_MCQA_knowledge_test.json` |
| Training | `MedQA/result/RAG_MedQA_USS_test_train.json` | `MedMCQA/result/Med_MCQA_knowledge_test_train.json` |

These are local derivatives, not complete official splits. Raw MedQA JSONL and raw MedMCQA option records cannot replace the `messages` JSON arrays expected by the Jamba scripts. Evaluation also reads `answer_idx`. Historical training filenames do not guarantee separation from test samples; sampling/split provenance remains to be documented.

## Dataset preprocessing

Preserve the online sequence: textbook chunks → vector store → retrieval → explanations → train/test conversation format. The original Chinese guide documents this process, but not every implementation is present in the clean project. Missing scripts below are not presented as runnable local commands.

### Convert text to JSON

Input: English/Chinese textbooks; output: JSON chunks. The online entry is [`txt2json.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/txt2json.py). Neither local project contains that filename. Its implementation must be supplied before rebuilding from textbooks.

### Vectorize JSON text

Encode chunks with an embedding model and build the retrieval store. The online entry is [`vector_store.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/vector_store.py). No matching script or vector index is present locally; the original project only retains some `embedding.py`/`config.py` support code.

### Retrieve knowledge for training and test questions

The online entry is [`generate_question_with_knowledges.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/generate_question_with_knowledges.py), using questions or questions plus options, with `retriever.py` and embedding configuration.

The original project has `dataset_handle/generate_question_with_knowledges_mcqa.py` and `generate_mcqa_question_with_knowledges.py`, but their imported `retriever.py` is absent locally. These scripts have not been migrated. Existing knowledge-augmented datasets can still feed the downstream experiments.

### Generate Chinese explanations

An external model uses prompts and retrieved context to produce explanations. The online implementation is under [`MultiProcessingLLM/`](https://github.com/julienamaury/Medical-Answering-Model-202410/tree/main/data/MedQA/utils/MultiProcessingLLM). The original `dataset_handle/` contains batch callers, API wrappers and an English prompt configuration; these are not migrated or a verified complete Chinese generation environment.

### Build standardized Chinese datasets

The online entry is [`format_json_dataset_for_training_llm.py`](https://github.com/julienamaury/Medical-Answering-Model-202410/blob/main/data/MedQA/utils/format_json_dataset_for_training_llm.py). The original project has the same filename plus an MCQA variant, neither currently migrated.

The reference additionally registers `dataset_info.json` for LLaMA-Factory. Existing Jamba scripts read JSON directly and do not require this registry. Training records contain assistant targets; inference removes assistant messages when constructing prompts.

Full historical parameter examples remain in the unchanged [original Chinese guide](readme/Jamba模型操作说明.md). Historical paths do not imply that corresponding implementations exist in this clean project.

## Fine-tuning and testing

Continue executing the original filenames. Absolute data paths avoid confusion with the online `data/MedQA/` layout and historical server `USMLE/MCQA/` directories. Existing `os.path.join` calls accept these paths without code changes.

```bash
PROJECT='/path/to/ZhiyiChat(MedQA)'
cd "$PROJECT/jamba"
mkdir -p results
```

Configure model paths, GPU counts and sampling parameters in the scripts. Set the training output root inside `jamba16mini_finetune.py` and the adapter root via `peft_fixed_path` in post-training inference. Their defaults still refer to the original server.

### Fine-tuning

```bash
# MedQA
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedQA/result/RAG_MedQA_USS_test_train.json"
# MedMCQA
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test_train.json"
```

Arguments are model directory name and dataset path. Original LoRA settings, SFTTrainer and save behavior are unchanged. Adapters are saved under the configured `finetune_result/<model_name>/<dataset_name>/`; use actual checkpoint names.

### Testing

```bash
# Mini plain inference on both datasets
python jamba16mini_inference.py AI21-Jamba-Mini-1.6 "$PROJECT/MedQA/result/MedQA_USS_test.json" "$PROJECT/MedMCQA/result/Med_MCQA_test.json"
# Large knowledge-augmented inference on both datasets
python jamba16large_inference.py AI21-Jamba-Large-1.6 "$PROJECT/MedQA/result/RAG_MedQA_USS_test.json" "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test.json"
# Post-training Mini inference: replace the final argument with the real adapter directory
python jamba16mini_inference_by_finetune.py AI21-Jamba-Mini-1.6 "$PROJECT/MedMCQA/result/Med_MCQA_knowledge_test.json" /path/to/actual-adapter
```

Either base script can use plain or knowledge-augmented records. Post-training inference merges into `merged/` under the adapter directory and then runs inference in the same process. Excel outputs go to `results/` relative to the working directory.

### Standardize results and calculate accuracy

The Jamba scripts directly write per-question Excel results and calculate accuracy, so the online LLaMA-Factory JSONL-to-Excel entry is unnecessary here. To re-extract answers:

```bash
cd "$PROJECT/utils"
python extract_answer.py --directory "$PROJECT/jamba/results"
```

This overwrites original result files using the existing regex logic. Denominators, matching and exception behavior have not been changed.

### Batch testing

Inference supports multiple data filenames, as above. The reference also includes temperature/top-p/checkpoint sweeps and aggregated experiment scores. No equivalent scheduler or cross-experiment summary script is currently provided; multiple input files are not a full parameter sweep.

## Project files and publication preparation

```text
jamba/       Four original Jamba 1.6 scripts
utils/       extract_answer.py
MedQA/       Original questions/textbooks and prepared inputs
MedMCQA/     Original and prepared inputs
readme/      Original bilingual guides and online comparison
```

Two duplicate/broken legacy MCQA inference scripts and the v0.1 trainer were removed. The four core Jamba scripts remain unchanged, with no unified CLI or workflow framework.

`.gitignore` excludes `MedQA/` and `MedMCQA/` from this code release while preserving local copies. Dataset files are not present in the current commit history, and no LFS objects need to be uploaded.

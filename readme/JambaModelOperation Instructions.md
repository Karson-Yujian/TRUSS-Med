Jamba Model Operation Instructions

1. Overview
This instruction comprehensively covers the inference operations of the large and mini versions of the Jamba model, as well as the fine - tuning and post - fine - tuning inference usage methods of the Jamba mini version, providing comprehensive guidance for related operations.

2. Environment Preparation
2.1 Installation of Dependent Libraries
Ensure the following dependent libraries are installed to ensure the normal operation of model - related operations:
vllm
torch
transformers
peft
pandas
tqdm

2.2 Path Description
Source Code Directory: /work/home/acbjfbaxkm/Jamba-Test
The following key files are included in this directory:
jamba16large_inference.py
jamba16mini_finetune.py
jamba16mini_inference.py
jamba16mini_inference_by_finetune.py
Jamba Model Main Path: /work/home/acbjfbaxkm/AI21Labs
This directory contains:
AI21-Jamba-Mini-1.6
AI21-Jamba-Large-1.6
Directories with suffixes such as <_nept_k4>, <_nept_k6>, <_nept_k....>, which are obtained by modifying the value corresponding to num_experts_per_tok in line 26 of config.json (the original value is 2).
Dataset Main Path: /work/home/acbjfbaxkm/DataSet
This directory contains:
USMLE Directory
RAG_MedQA_USS_test_train.json: Training dataset (354 items)
MedQA_USS_test.json: Dataset without knowledge (354 items)
RAG_MedQA_USS_test.json: Dataset with knowledge (354 items)
MCQA Directory
Med_MCQA_knowledge_test_train.json: Training dataset (300 items)
Med_MCQA_test.json: Dataset without knowledge (300 items)
Med_MCQA_knowledge_test.json: Dataset with knowledge (300 items)


3. Inference of Jamba 16 Large Version
3.1 Code File
jamba16large_inference.py
3.2 Execution Steps
Set Parameters: Ensure that parameters such as fixed_path, dataset_path, temperature, top_k, and top_p in the code are set correctly.
Execute Command:
python jamba16large_inference.py <model_name> <dataset_filenames>

3.3 Parameter Description
<model_name>: The name of the model, such as AI21-Jamba-Large-16.
<dataset_filenames>: The filenames of the datasets. Multiple filenames can be passed in, separated by spaces, such as dataset1.json dataset2.json.
3.4 Example
python jamba16large_inference.py AI21-Jamba-Large-1.6 USMLE/MedQA_USS_test.json

4. Inference of Jamba 16 Mini Version
4.1 Code File
jamba16mini_inference.py
4.2 Execution Steps
Set Parameters: Ensure that parameters such as fixed_path, dataset_path, temperature, top_k, and top_p in the code are set correctly.
Execute Command:
python jamba16mini_inference.py <model_name> <dataset_filenames>

4.3 Parameter Description
<model_name>: The name of the model, such as AI21-Jamba-Mini-1.6.
<dataset_filenames>: The filenames of the datasets. Multiple filenames can be passed in, separated by spaces, such as dataset1.json dataset2.json.
4.4 Example
python jamba16mini_inference.py AI21-Jamba-Mini-1.6 USMLE/MedQA_USS_test.json

5. Finetune of Jamba 16 Mini Version
5.1 Code File
jamba16mini_finetune.py
5.2 Execution Steps
Set Parameters: The model name and dataset path can be set through command - line parameters.
Execute Command:
python jamba16mini_finetune.py <model_name> <dataset_path>

5.3 Parameter Description
<model_name>: The name of the model, such as AI21-Jamba-Mini-1.6.
<dataset_path>: The path of the dataset, such as RAG_MedQA_USS_test_train.json.
5.4 Example
python jamba16mini_finetune.py AI21-Jamba-Mini-1.6 RAG_MedQA_USS_test_train.json

5.5 Finetune Results
The save directory is /work/home/acbjfbaxkm/Jamba-Test/finetune_result.
6. Inference after Finetune of Jamba 16 Mini Version
6.1 Code File
jamba16mini_inference_by_finetune.py
6.2 Execution Steps
Set Parameters: Ensure that parameters such as fixed_path, dataset_path, temperature, top_k, top_p, and peft_fixed_path in the code are set correctly.
Execute Command:
python jamba16mini_inference_by_finetune.py <model_name> <dataset_filenames> <peft_relative_path>

6.3 Parameter Description
<model_name>: The name of the model, such as AI21-Jamba-Mini-1.6.
<dataset_filenames>: The filenames of the datasets. Multiple filenames can be passed in, separated by spaces, such as dataset1.json dataset2.json.
<peft_relative_path>: The relative path of the Peft model. The fixed path is /work/home/acbjfbaxkm/Jamba-Test/finetune_result, and only the relative path needs to be entered, such as AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300.
6.4 Example
python jamba16mini_inference_by_finetune.py AI21-Jamba-Mini-1.6 MCQA/Med_MCQA_knowledge_test AI21-Jamba-Mini-1.6/Med_MCQA_knowledge_test_train/checkpoint-300

6.5 Description
Before inference, the code will merge the original model (such as AI21-Jamba-Mini-1.6) with the fine - tuned lora weights into the merged directory under the peft_relative_path.
7. Result Saving
The inference results will be saved to the /work/home/acbjfbaxkm/Jamba-Test/results directory, and the filename format is:
jamba16<version>_inference_<related_information>_temperature<temperature_value>_topp<top_p_value>_topk<top_k_value>_<timestamp>.xlsx

8. Description of Inference Answer Extraction
There is a function <extract_predicted_option_by_us> in the inference code to extract the answer replied by the model.
If a new model output answer format is encountered, the corresponding expression can be added to the function <extract_predicted_option_by_us>.
extract_answer.py is used to reprocess the answer replied by the model in the extraction result file (.xlsx).
Usage example:
python extract_answer.py --directory /path/to/your/directory

Please adjust the parameters and paths in the above instructions according to the actual situation.
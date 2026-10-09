import pandas as pd
import os
import re
import argparse

# 定义数字到字母的映射
NUMBER_TO_LETTER = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E'
}


# 定义答案提取函数 - 增强版，支持数字选项并转换为字母
def extract_answer(text):
    if not isinstance(text, str):
        return None

    # 定义可能的答案格式的正则表达式模式
    patterns = [
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
            if answer in NUMBER_TO_LETTER:
                return NUMBER_TO_LETTER[answer]
            return answer[0].upper() if answer else None

    return None


# 处理单个Excel文件
def process_excel_file(file_path):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 检查是否包含所需的列
        required_columns = ['Question', 'Correct Answer', 'Predicted Option', 'Generated Text', 'Correct']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"文件 {file_path} 缺少必要的列: {', '.join(missing_columns)}")
            return False

        # 确保'Correct'列的数据类型为布尔型
        if 'Correct' in df.columns:
            df['Correct'] = df['Correct'].astype(bool)
        else:
            df['Correct'] = False  # 创建布尔类型的列

        for index, row in df.iterrows():
            # 从Generated Text中提取答案
            extracted_answer = extract_answer(row['Generated Text'])
            if extracted_answer:
                # 更新Predicted Option列
                df.at[index, 'Predicted Option'] = extracted_answer

                # 比较提取的答案与Correct Answer
                correct_answer = str(row['Correct Answer']).strip()
                # 明确将比较结果转换为布尔类型
                is_correct = correct_answer == extracted_answer
                df.at[index, 'Correct'] = is_correct

        # 保存修改后的DataFrame到原文件（覆盖）
        df.to_excel(file_path, index=False)
        #print(f"已成功处理并保存文件: {file_path}")

        # 计算准确率
        accuracy = df['Correct'].mean()

        # 提取文件名中inference和temperature之间的部分
        file_name = os.path.basename(file_path)
        match = re.search(r'inference(.*)temperature', file_name)
        if match:
            part = match.group(1).strip()
            print(f"文件名部分: {part}, 准确率: {accuracy * 100:.2f}%")
        else:
            print(f"未在文件名 {file_name} 中找到 'inference' 和 'temperature' 之间的部分")

        return True
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {str(e)}")
        return False


# 处理目录中的所有Excel文件
def process_excel_files_in_directory(directory):
    # 获取目录中所有Excel文件
    excel_files = [f for f in os.listdir(directory) if f.lower().endswith(('.xlsx', '.xls'))]

    if not excel_files:
        print(f"目录 {directory} 中没有找到Excel文件")
        return

    # 处理每个Excel文件
    for file in excel_files:
        file_path = os.path.join(directory, file)
        process_excel_file(file_path)


# 主函数
def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='Process Excel files in a directory.')
    # 添加目录路径参数，默认处理仓库内 jamba/results 目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_results_dir = os.path.join(project_root, 'jamba', 'results')
    parser.add_argument('--directory', type=str, default=default_results_dir,
                        help='Directory path containing Excel files to process.')

    # 解析命令行参数
    args = parser.parse_args()

    # 指定要处理的目录路径（修改为你的目录）
    directory_path = args.directory

    if not os.path.isdir(directory_path):
        print(f"错误: 目录 '{directory_path}' 不存在")
        return

    process_excel_files_in_directory(directory_path)
    print("所有文件处理完成！")


if __name__ == "__main__":
    main()

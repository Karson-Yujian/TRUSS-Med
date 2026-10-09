import json
import sys

def count_choice_types(file_path):
    """
    统计JSON文件中choice_type字段为single和multi的元素数量
    
    Args:
        file_path: JSON文件路径
    """
    single_count = 0
    multi_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 假设文件中每一行是一个JSON对象
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    # 解析每一行的JSON对象
                    data = json.loads(line)
                    
                    # 检查是否存在choice_type字段
                    if 'choice_type' in data:
                        choice_type = data['choice_type']
                        
                        if choice_type == 'single':
                            single_count += 1
                        elif choice_type == 'multi':
                            multi_count += 1
                        else:
                            print(f"警告: 第{line_num}行发现未知的choice_type值: {choice_type}")
                    else:
                        print(f"警告: 第{line_num}行缺少choice_type字段")
                
                except json.JSONDecodeError as e:
                    print(f"错误: 第{line_num}行不是有效的JSON格式 - {e}")
    
    except FileNotFoundError:
        print(f"错误: 文件不存在 - {file_path}")
        return
    except Exception as e:
        print(f"错误: 读取文件时发生异常 - {e}")
        return
    
    # 计算总量
    total_count = single_count + multi_count
    
    # 打印统计结果
    print("=" * 50)
    print(f"JSON文件 '{file_path}' 统计结果:")
    print(f"choice_type为'single'的元素数量: {single_count}")
    print(f"choice_type为'multi'的元素数量: {multi_count}")
    print(f"总元素数量: {total_count}")
    print("=" * 50)

def main():
    if len(sys.argv) != 2:
        print("用法: python script.py <json_file_path>")
        print("示例: python script.py data.json")
        return
    
    file_path = sys.argv[1]
    count_choice_types(file_path)

if __name__ == "__main__":
    main()

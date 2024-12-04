from pathlib import Path
import re
from typing import List

def read_input(file_name: str) -> str:
    return (Path(__file__).parent / file_name).read_text()

def find_operations(input: str, include_enablers: bool = False) -> List[str]:
    pattern = r'(mul\(\d*,\d*\))' if not include_enablers else r'(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))'
    matches = re.findall(pattern, input)
    return ["".join(val for val in match if val) for match in matches]

def multiply_inside(operations: List[str]) -> List[int]:
    translation_table = str.maketrans({"m": "", "u": "", "l": "", "(": "", ")": ""})
    result:list[int] = []
    enabler = True
    
    for operation in operations:
        translated = operation.translate(translation_table)
        
        if translated == "don't":
            enabler = False
            continue
        elif translated == "do":
            enabler = True
            continue
            
        if enabler and ',' in translated:
            a, b = map(int, translated.split(','))
            result.append(a * b)
    
    return result

def main():
    content = read_input("data/inputData.txt")
    
    # Part 1: Without enablers
    multiply_list = multiply_inside(find_operations(content))
    
    # Part 2: With enablers
    multiply_list_enabled = multiply_inside(find_operations(content, include_enablers=True))
    
    print(f'without = {sum(multiply_list)} with enablers = {sum(multiply_list_enabled)}')

if __name__ == "__main__":
    main()

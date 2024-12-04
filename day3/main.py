from pathlib import Path
import re

def read_input(file_name: str):
    input_path = Path(__file__).parent / file_name
    with open(input_path, 'r') as file:
        return file.read()

def find_valid_operations(input:str) -> list[str]:
    return re.findall(r'(mul\(\d*,\d*\))', input)

def find_valid_with_enablers(input:str) -> list[str]:
    valids = re.findall(r'(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))', input)
    valid_list = ["".join(str(val) for val in valid if val != "") for valid in valids]

    return valid_list 


def multiply_inside(operations: list[str]) -> list[int]:
    translation_table = str.maketrans({
        "m": "",
        "u": "",
        "l": "",
        "(": "",
        ")": ""
    })
    result: list[int] = []

    enabler = True
    for row in operations:
        translated = [value for value in row.translate(translation_table).split(',')]
        for item in translated:
            if(item == "don't"):
                enabler = False
            elif(item=="do"):
                enabler = True
            if(enabler and item.isnumeric()):
                result.append(*[int(a) * int(b) for a, b in zip(translated[:-1], translated[1:])])
            break
            
        
    return result

def main():
    content = read_input("data/inputData.txt")
    valid_input = find_valid_operations(content)
    valid_with_enablers = find_valid_with_enablers(content)
    multiply_list = multiply_inside(valid_input)
    multiply_list_enabled = multiply_inside(valid_with_enablers)
    print(f'without = {sum(multiply_list)} with enablers = {sum(multiply_list_enabled)}')


if __name__ == "__main__":
    main()

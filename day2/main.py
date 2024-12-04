from pathlib import Path

def read_input(file_name: str):
    input_path = Path(__file__).parent / file_name
    with open(input_path, 'r') as file:
        return file.readlines()

def main():
    data = read_input('data/inputData.txt')
    reports = [[int(num) for num in item.strip().split()] for item in data]
    safety_count = 0

    for report in reports:
        mayor = False
        minor = False
        safety_leap = 0

        for index in range(len(report)-1):
            if(report[index] > report[index+1]):
                mayor = True
                safety_leap = report[index] - report[index+1]

            elif(report[index] < report[index+1]):
                minor = True
                safety_leap = report[index+1]- report[index] 
            else:
                safety_leap = 0
            
            if(mayor and minor or safety_leap > 3 or safety_leap < 1):
                mayor = False
                minor = False

            if(not mayor and not minor):
                break

        if(mayor or minor):
            safety_count += 1
    
    print(f'Safety count = {safety_count}')
            
if __name__ == "__main__":
    main()
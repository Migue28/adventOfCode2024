def main():
    left_list: list[str] = []
    right_list: list[str] = []
    file_path = 'data/inputData.txt'
    with open(file_path, 'r') as file:
        data = file.readlines()
        for line in data:
            left_list.append(line.split(" ")[0])
            right_list.append(line.split(" ")[3].split('\n')[0])
    
    left = [int(item) for item in left_list ]
    right = [int(item) for item in right_list ]

    left.sort()
    right.sort()

    total = 0
    
    for i in range(len(left)):
        total += abs(left[i] - right[i]) 

    print(total)


if __name__ == "__main__":
    main()

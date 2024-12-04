def main():
    left_list: list[str] = []
    right_list: list[str] = []
    file_path = 'data/inputData.txt'
    with open(file_path, 'r') as file:
        data = file.readlines()
        for line in data:
            left_list.append(line.split(" ")[0])
            right_list.append(line.split(" ")[3].split('\n')[0])
    
    lefts = [int(item) for item in left_list ]
    rights = [int(item) for item in right_list ]

    lefts.sort()
    rights.sort()

    total = 0
    
    for left, right in zip(lefts, rights):
        total += abs(left - right) 

    print(f'Difference total = {total}')

    similary_score = 0

    for left, right in zip(lefts, rights):
        similary_score += left * rights.count(left)

    print(f'Similary score = {similary_score}')


if __name__ == "__main__":
    main()

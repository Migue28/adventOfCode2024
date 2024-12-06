from pathlib import Path


def read_input(file_name: str) -> str:
    return (Path(__file__).parent / file_name).read_text()


def divide_list(data: str) -> tuple[list[str], list[str]]:
    content = data.split()
    rules = [val for val in content if "|" in val]
    prints = [val for val in content if "," in val]

    return rules, prints


def pick_rules(rules: list[str], print_value: str):
    selected_rules = [rule for rule in rules if print_value in rule]
    return selected_rules


def count_valid(valid_list: list[bool]) -> bool:
    return False not in valid_list


def check_rule(rules: list[str], print_value: str, print_line: list[str]) -> bool:
    current_index = print_line.index(print_value)
    valid_list: list[bool] = []
    for index, val in enumerate(print_line):
        for rule in rules:
            if val == rule:
                if current_index < index:
                    valid_list.append(True)
                else:
                    valid_list.append(False)
    return count_valid(valid_list)


def check_line(rules: list[str], print_line: str, sort_list: bool = False) -> int:
    selected_rules = [pick_rules(rules, line) for line in print_line.split(",")]
    print_list = print_line.split(",")
    valid_list: list[bool] = []

    for i, line in enumerate(print_list):
        rule = selected_rules[i]
        valid_list.append(
            check_rule(
                [rul.split("|")[1] for rul in rule if rul.split("|")[1] != line],
                line,
                print_list,
            )
        )
    if sort_list and count_valid(valid_list):
        print_list.sort(reverse=True)
        print(print_list)
        return int(print_list[int((len(print_list) / 2))])

    if count_valid(valid_list):
        return int(print_list[int((len(print_list) / 2))])
    return 0


def main():
    data = read_input("data/example.txt")
    rules, prints = divide_list(data)

    print(sum([check_line(rules, print_line, True) for print_line in prints]))


if __name__ == "__main__":
    main()

from pathlib import Path
from typing import Callable

rotate_directions: dict[str, Callable[[int, int], tuple[int, int, str]]] = {
    "up": lambda y, x: (y, x + 1, "right"),  # → (moves right)
    "right": lambda y, x: (y + 1, x, "down"),  # ↓ (moves down)
    "down": lambda y, x: (y, x - 1, "left"),  # ← (moves left)
    "left": lambda y, x: (y - 1, x, "up"),  # ↑ (moves up)
}

keep_moving: dict[str, Callable[[int, int], tuple[int, int, str]]] = {
    "up": lambda y, x: (y - 1, x, "up"),  # ↑ (moves up)
    "right": lambda y, x: (y, x + 1, "right"),  # → (moves right)
    "down": lambda y, x: (y + 1, x, "down"),  # ↓ (moves down)
    "left": lambda y, x: (y, x - 1, "left"),  # ← (moves left)
}


def read_input(file_name: str):
    input_path = Path(__file__).parent / file_name
    with open(input_path, "r") as file:
        return file.readlines()


def find_guard_position(map: list[str], guard: str) -> tuple[int, int]:
    for y, row in enumerate(map):
        if guard in row:
            return y, row.index(guard)
    return -1, -1


def change_direction(coordinates: tuple[int, int, str]) -> tuple[int, int, str]:
    y, x, direction = coordinates
    return rotate_directions[direction](y, x)


def go_forward(coordinates: tuple[int, int, str]) -> tuple[int, int, str]:
    y, x, direction = coordinates
    return keep_moving[direction](y, x)


def is_inside(y_len: int, x_len: int, coordinates: tuple[int, int, str]) -> bool:
    y, x, *_ = coordinates
    return 0 <= y < y_len and 0 <= x < x_len


def move_guard(
    y_len: int,
    x_len: int,
    map: list[str],
    coordinates: tuple[int, int, str],
    obstacle: str = "#",
) -> tuple[int, int, str]:
    old_coordinates = coordinates
    y, x, direction = go_forward(old_coordinates)
    if is_inside(y_len=y_len, x_len=x_len, coordinates=(y, x, direction)):
        if map[y][x] == obstacle:
            new_coordinates = change_direction(coordinates)
            write_map_cell(map, new_coordinates)
            return new_coordinates
        else:
            new_coordinates = (y, x, direction)
            write_map_cell(map, new_coordinates)
            return new_coordinates
    return (y, x, direction)


def write_map_cell(map: list[str], coordinates: tuple[int, int, str]):
    new_map = map
    y, x, *_ = coordinates
    string = list(map[y])
    string[x] = "X"
    new_map[y] = "".join(string)


def main():
    file_path = "data/input.txt"
    map = [line.split("\n")[0] for line in read_input(file_path)]
    y, x = find_guard_position(map, "^")
    direction = "up"
    y_len = len(map)
    x_len = len(map[0])
    coordinates = (y, x, direction)
    while is_inside(y_len=y_len, x_len=x_len, coordinates=coordinates):
        coordinates = move_guard(
            y_len=y_len, x_len=x_len, map=map, coordinates=coordinates
        )
        # print(
        #     f"coordinates {coordinates} is inside {is_inside(y_len=y_len, x_len=x_len, coordinates=coordinates)}"
        # )
    print(map)
    x_count = [cell.count("X") for cell in map]
    guard_count = [cell.count("^") for cell in map]
    print(f"Salió en {coordinates} con {sum(x_count + guard_count)} pasos")


if __name__ == "__main__":
    main()

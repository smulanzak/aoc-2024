# Correct answer for Part 1: 526.
# Correct answer for Part 2: 566.

import copy

EXAMPLE = "python/day02/example.txt"
INPUT = "python/day02/input.txt"

def parse(input: str) -> list[list[int]]:
    levels_list = []
    with open(input) as f:
        for line in f.readlines():
            levels_list.append(list(map(int, line.split('\n')[0].split(' '))))
    return levels_list

def safe(levels: list[int], part: int) -> bool:
    outcome = validate(get_validation_list(levels))
    match part:
        case 1:
            return outcome
        case 2:
            return outcome or True in [validate(get_validation_list(remove_index(levels, i))) for i in range(len(levels))]

def get_validation_list(levels: list[int]) -> list[int]:
    return [levels[i]-levels[i+1] for i in range(len(levels)-1)]

def remove_index(levels: list[int], index: int) -> list[int]:
    levels_copy = copy.deepcopy(levels)
    levels_copy.pop(index)
    return levels_copy

def validate(distances: list[int]) -> bool:
    lower = -4 if distances[0] < 0 else 0
    upper = 0 if distances[0] < 0 else 4
    for distance in distances:
        if distance <= lower or distance >= upper:
            return False
    return True

def safe_count(level_list: list[list[int]], part: int) -> int:
    return sum([safe(levels, part) for levels in level_list])

def solve1(levels_list: list[list[int]]) -> int:
    return safe_count(levels_list, part=1)

def solve2(levels_list: list[list[int]]) -> int:
    return safe_count(levels_list, part=2)

def test() -> None:
    levels_list = parse(EXAMPLE)
    assert solve1(levels_list) == 2
    assert solve2(levels_list) == 4

def main() -> None:
    levels_list = parse(INPUT)
    print(f"Answer for part 1: {solve1(levels_list)}.")
    print(f"Answer for part 2: {solve2(levels_list)}.")

if __name__ == "__main__":
    test()
    main()

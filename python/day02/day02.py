# Correct answer for Part 1: 526.
# Correct answer for Part 2: 566.

import copy

EXAMPLE = "python/day02/day02.example"
INPUT = "python/day02/day02.input"

def parse(input: str) -> list[list[int]]:
    with open(input) as f:
        return [list(map(int, line.split('\n')[0].split(' '))) for line in f.readlines()]

def remove_index(levels: list[int], index: int) -> list[int]:
    levels_copy = copy.deepcopy(levels)
    levels_copy.pop(index)
    return levels_copy

def validate_base(levels: list[int]) -> bool:
    return validate_distance(levels) and (validate_order(levels) or validate_order(levels, -1))

def validate_distance(levels: list[int]) -> bool:
    return all([abs(levels[i]-levels[i+1]) in [1, 2, 3] for i in range(len(levels)-1)])

def validate_order(levels: list[int], order=0) -> bool:
    return all([levels[i] < levels[i+1] if order >= 0 else levels[i] > levels[i+1] for i in range(len(levels)-1)])

def validate_removed(levels: list[int]) -> bool:
    return validate_base(levels) or any([validate_base(remove_index(levels, i)) for i in range(len(levels))])

def solve1(levels_list: list[list[int]]) -> int:
    return sum([validate_base(levels) for levels in levels_list])

def solve2(levels_list: list[list[int]]) -> int:
    return sum([validate_removed(levels) for levels in levels_list])

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

# Correct answer for Part 1: 7198.
# Correct answer for Part 2: 4230.

EXAMPLE = "python/day05/day05.example"
INPUT = "python/day05/day05.input"

def parse(input: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules, updates = [], []
    sep = False
    with open(input) as f:
        for line in f.readlines():
            if line == '\n':
                sep = True
                continue
            if sep:
                updates.append(list(map(int, line.split('\n')[0].split(','))))
            else:
                rules.append(tuple(map(int, line.split('\n')[0].split('|'))))
    return rules, updates

def get_order_validations(rules: list[tuple[int, int]], update: list[int]) -> list[bool]:
    return [(update[i], update[i+1]) in rules for i in range(len(update)-1)]

def get_correct_order(rules: list[tuple[int, int]], update: list[int]) -> list[int]:
    while not all(order := get_order_validations(rules, update)):
        for i in range(len(order)):
            if not order[i]:
                update[i], update[i+1] = update[i+1], update[i]
    return update

def sum_middle(rules: list[tuple[int, int]], updates: list[list[int]], part: int) -> int:
    sum = 0
    for update in updates:
        if part == 1 and all(get_order_validations(rules, update)):
            sum += get_middle(update)
        if part == 2 and not all(get_order_validations(rules, update)):
            sum += get_middle(get_correct_order(rules, update))
    return sum

def get_middle(update: list[list[int]]) -> int:
    return update[len(update)//2]

def solve1(rules: tuple[list[int]], updates: list[list[int]]) -> int:
    return sum_middle(rules, updates, part=1)

def solve2(rules: tuple[list[int]], updates: list[list[int]]) -> int:
    return sum_middle(rules, updates, part=2)

def test() -> None:
    rules, updates = parse(EXAMPLE)
    assert solve1(rules, updates) == 143
    assert solve2(rules, updates) == 123

def main() -> None:
    rules, updates = parse(INPUT)
    print(f"Answer for part 1: {solve1(rules, updates)}.")
    print(f"Answer for part 2: {solve2(rules, updates)}.")

if __name__ == "__main__":
    test()
    main()

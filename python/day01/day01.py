# Correct answer for Part 1: 2904518.
# Correct answer for Part 2: 18650129.

from collections import Counter

EXAMPLE = "python/day01/day01.example"
INPUT = "python/day01/day01.input"

def parse(input: str) -> list[tuple[int, int]]:
    left, right = [], []
    with open(input) as f:
        for line in f.readlines():
            l, r = line.split('\n')[0].split('   ')
            left.append(int(l))
            right.append(int(r))
    return list(zip(sorted(left), sorted(right)))

def solve1(ids: list[tuple[int, int]]) -> int:
    return sum([abs(x - y) for x, y in ids])

def solve2(ids: list[tuple[int, int]]) -> int:
    left, right = zip(*ids)
    return sum([x * Counter(right)[x] for x in left])

def test() -> None:
    ids = parse(EXAMPLE)
    assert solve1(ids) == 11
    assert solve2(ids) == 31

def main() -> None:
    ids = parse(INPUT)
    print(f"Answer for part 1: {solve1(ids)}.")
    print(f"Answer for part 2: {solve2(ids)}.")

if __name__ == "__main__":
    test()
    main()

# Correct answer for Part 1: 2904518.
# Correct answer for Part 2: 18650129.

EXAMPLE = "python/day01/example.txt"
INPUT = "python/day01/input.txt"

def parse(input: str) -> list[list[int], list[int]]:
    left, right = [], []
    with open(input) as f:
        for line in f.readlines():
            l, r = ' '.join(line.split('\n')[0].split(' ')).split()
            left.append(int(l))
            right.append(int(r))
    return sorted(left), sorted(right)

def solve1(left: list[int], right: list[int]) -> int:
    return sum([abs(left[i] - right[i]) for i in range(len(left))])

def solve2(left: list[int], right: list[int]) -> int:
    return sum(left[i] * right.count(left[i]) for i in range(len(left)))

def test() -> None:
    left, right = parse(EXAMPLE)
    assert solve1(left, right) == 11
    assert solve2(left, right) == 31

def main() -> None:
    left, right = parse(INPUT)
    print(f"Answer for part 1: {solve1(left, right)}.")
    print(f"Answer for part 2: {solve2(left, right)}.")

if __name__ == "__main__":
    test()
    main()

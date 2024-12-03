# Correct answer for Part 1: 189600467.
# Correct answer for Part 2: 107069718.

import re

PATTERNS = [r'mul\(\d{1,3},\d{1,3}\)', r'(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don\'t\(\))']
EXAMPLES = ["python/day03/day03.example1", "python/day03/day03.example2"]
INPUT = "python/day03/day03.input"

def parse(input: str, part: int) -> list[str]:
    with open(input) as f:
        return re.findall(PATTERNS[0], f.read()) if part == 1 else re.findall(PATTERNS[1], f.read())

def multiply(instruction: str) -> int:
    i, j = tuple(map(int, instruction.split('(')[-1].split(')')[0].split(',')))
    return int(i * j)

def get_enabled_instructions(instructions: list[str]) -> list[str]:
    output = []
    enabled = True
    for instruction in instructions:
        enabled = False if instruction == "don't()" else True if instruction == "do()" else enabled
        if "mul" in instruction and enabled:
            output.append(instruction)
    return output

def solve1(instructions: list[str]) -> int:
    return sum([multiply(instruction) for instruction in instructions])

def solve2(instructions: list[str]) -> int:
    return sum([multiply(instruction) for instruction in get_enabled_instructions(instructions)])

def test() -> None:
    assert solve1(parse(EXAMPLES[0], part=1)) == 161
    assert solve2(parse(EXAMPLES[1], part=2)) == 48

def main() -> None:
    print(f"Answer for part 1: {solve1(parse(INPUT, part=1))}.")
    print(f"Answer for part 2: {solve2(parse(INPUT, part=2))}.")

if __name__ == "__main__":
    test()
    main()

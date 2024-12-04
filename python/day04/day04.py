# Correct answer for Part 1: 2613.
# Correct answer for Part 2: 1905.

import re

PATTERN = r'(?=(XMAS)|(SAMX))'
EXAMPLE = "python/day04/day04.example"
INPUT = "python/day04/day04.input"

def parse(input: str) -> list[str]:
    with open(input) as f:
        return [line.split('\n')[0] for line in f.readlines()]

def count_horizontal(rows: list[str]) -> int:
    return sum([len(re.findall(PATTERN, row)) for row in rows])

def count_vertical(rows: list[str]) -> int:
    return sum([len(re.findall(PATTERN, row)) for row in [''.join(t) for t in list(zip(*rows))]])

def get_diagonals(rows: list[str], lock="col") -> list[str]:
    diagonals = []
    for i in range(len(rows)-3):
        string = ""
        j = 0
        while i+j < len(rows):
            string += rows[j][i+j] if lock == "col" else rows[i+j][j]
            j += 1
        diagonals.append(string)
    return diagonals

def count_diagonals(rows: list[str]) -> int:
    # Don't count the first diagonal twice for any direction
    diagonals = get_diagonals(rows)[1:] + get_diagonals(rows, lock="row") + get_diagonals(reverse(rows))[1:] + get_diagonals(reverse(rows), lock="row")
    return sum([len(re.findall(PATTERN, row)) for row in diagonals])

def reverse(rows: list[str]) -> list[str]:
    return [row[::-1] for row in rows]

def count_all(rows: list[str]) -> int:
    return count_horizontal(rows) + count_vertical(rows) + count_diagonals(rows)

def count_xmas(rows: list[str]) -> int:
    count = 0
    for i in range(len(rows)-2):
        for j in range(len(rows)-2):
            if rows[i+1][j+1] == 'A':
                m_north = rows[i][j] == rows[i][j+2] == 'M' and rows[i+2][j] == rows[i+2][j+2] == 'S'
                m_east = rows[i][j+2] == rows[i+2][j+2] == 'M' and rows[i][j] == rows[i+2][j] == 'S'
                m_south = rows[i+2][j] == rows[i+2][j+2] == 'M' and rows[i][j] == rows[i][j+2] == 'S'
                m_west = rows[i][j] == rows[i+2][j] == 'M' and rows[i][j+2] == rows[i+2][j+2] == 'S'
                count += any([m_north, m_east, m_south, m_west])
    return count

def solve1(rows: list[str]) -> int:
    return count_all(rows)

def solve2(rows: list[str]) -> int:
    return count_xmas(rows)

def test() -> None:
    assert solve1(parse(EXAMPLE)) == 18
    assert solve2(parse(EXAMPLE)) == 9

def main() -> None:
    print(f"Answer for part 1: {solve1(parse(INPUT))}.")
    print(f"Answer for part 2: {solve2(parse(INPUT))}.")

if __name__ == "__main__":
    test()
    main()

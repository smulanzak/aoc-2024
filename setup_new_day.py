import os
import sys

DAY = f"day{'0' if len(sys.argv[1]) == 1 else ''}{sys.argv[1]}"
EXAMPLE = "example.txt"
INPUT = "input.txt"
LANG = sys.argv[2]

def create_directory() -> None:
    os.chdir(LANG)
    os.mkdir(DAY)

def create_files() -> None:
    match LANG.lower():
        case "python":
            create_python_script()
        case "go":
            create_go_script()
    create_input_file()

def create_python_script() -> None:
    with open(f"{DAY}/{DAY}.py", 'w') as f:
        f.write(f'# Correct answer for Part 1:\n# Correct answer for Part 2:\n\nEXAMPLE = "{DAY}/example.txt"\nINPUT = "{DAY}/{INPUT}"\n\ndef solve1() -> None:\n    pass\n\ndef solve2() -> None:\n    pass\n\ndef main() -> None:\n    pass\n\nif __name__ == "__main__":\n    main()\n')

def create_go_script() -> None:
    with open(f"{DAY}/{DAY}.go", 'w') as f:
        f.write(f'package main\n\nimport (\n\t"fmt"\n)\n\nconst (\n\texample = "{DAY}/example.txt"\n\tinput   = "{DAY}/{INPUT}"\n)\n\nfunc solve1() int \u007b\n\treturn 1\n\u007d\n\nfunc solve2() int \u007b\n\treturn 2\n\u007d\n\nfunc main() \u007b\n\tfmt.Print(solve1()) // Correct answer for Part 1:\n\tfmt.Print(solve2()) // Correct answer for Part 2:\n\u007d')

def create_input_file() -> None:
    with open(f"{DAY}/{EXAMPLE}", 'w'):
        pass
    with open(f"{DAY}/{INPUT}", 'w'):
        pass

def validate_input() -> None:
    assert int(DAY[-2:]) in range(1, 26)
    assert LANG.lower() in ["go", "python"]

def main() -> None:
    validate_input()
    create_directory()
    create_files()

if __name__ == "__main__":
    main()

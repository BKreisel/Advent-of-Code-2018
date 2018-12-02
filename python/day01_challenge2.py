# Day 01
import os.path

INPUT_FILE = "day01.txt"


def open_input() -> str:
    project_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    input_path = os.path.join(project_dir, "input", INPUT_FILE)
    return open(input_path, "r")


def main():
    frequency: int = 0
    known_frequencies = set()
    while True:
        with open_input() as lines:
            for line in lines:
                frequency += parse_frequency_change(line)
                if frequency in known_frequencies:
                    print(f"Duplicated Frequency: {frequency}")
                    return
                known_frequencies.add(frequency)


def parse_frequency_change(line: str) -> int:
    delta = int(line[1:])
    if line[0] == "+":
        return delta
    if line[0] == "-":
        return -delta
    raise ValueError


if __name__ == "__main__":
    main()

from util import read_input

DAY = 1


def main():
    frequency: int = 0
    for line in read_input(DAY):
        frequency += change_frequency(line)
    print(f"Frequency: {frequency}")


def change_frequency(line: str) -> int:
    delta = int(line[1:])
    if line[0] == "+":
        return delta
    if line[0] == "-":
        return -delta
    raise ValueError


if __name__ == "__main__":
    main()

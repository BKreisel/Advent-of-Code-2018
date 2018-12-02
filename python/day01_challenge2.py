from util import read_input

DAY = 1


def main():
    frequency: int = 0
    known_frequencies = set()
    while True:
        for line in read_input(DAY):
            frequency += change_frequency(line)
            if frequency in known_frequencies:
                print(f"Duplicated Frequency: {frequency}")
                return
            known_frequencies.add(frequency)


def change_frequency(line: str) -> int:
    delta = int(line[1:])
    if line[0] == "+":
        return delta
    if line[0] == "-":
        return -delta
    raise ValueError


if __name__ == "__main__":
    main()

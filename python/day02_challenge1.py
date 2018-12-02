from typing import Dict, Tuple

from util import read_input

DAY = 2


def main():
    twos: int = 0
    threes: int = 0

    for line in read_input(DAY):
        two, three = validate_boxid(line.rstrip())
        if two:
            twos += 1
        if three:
            threes += 1

    checksum = threes * twos
    print(f"Checksum: {checksum}")


# Check of Box ID has 2 letter matches and 3 letter matches
def validate_boxid(box_id: str) -> Tuple[bool, bool]:
    letter_counts = count_letters(box_id)
    valid_two: bool = False
    valid_three: bool = False

    for letter, count in letter_counts.items():
        if count == 2:
            valid_two = True
        elif count == 3:
            valid_three = True
    return (valid_two, valid_three)


# Transform Box ID into Dict of Letter:Count
def count_letters(box_id: str) -> Dict[str, int]:
    letter_counts: Dict[str, int] = {}
    for letter in box_id:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


if __name__ == "__main__":
    main()

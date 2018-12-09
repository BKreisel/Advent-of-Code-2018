from util import read_input
from typing import Tuple

DAY = 5


def is_unit_match(unit1: str, unit2: str) -> bool:
    if unit1 == unit2:
        return False
    if unit1.upper() == unit2.upper():
        return True
    return False


# Remove case matching chars and return polymer + # modifications
def reduce(polymer: str) -> Tuple[str, bool]:
    units = list(polymer)
    reduced = False

    idx = 0
    units_len = len(units)
    while idx < units_len - 1:
        if is_unit_match(units[idx], units[idx + 1]):
            del(units[idx:idx + 2])
            reduced = True
            units_len = len(units)
        else:
            idx += 1
    return "".join(units), reduced


def collapse_polymer(polymer: str) -> int:
    while True:
        polymer, reduced = reduce(polymer)
        if not reduced:
            break
        print(f"\r\tPolymer Length: {len(polymer)}", end="       ")
    print("")
    return len(polymer)


def main():
    original = read_input(DAY)[0].rstrip()
    unique_chars = set([x.lower() for x in list(original)])
    polymer_lens = []

    for char in unique_chars:
        print(f"Character: {char.upper()}")
        polymer = "".join([x for x in list(original) if char not in [x.upper(), x.lower()]])
        polymer_lens.append(collapse_polymer(polymer))
    print(f"\nShortest Polymer: {min(polymer_lens)}")


if __name__ == "__main__":
    main()

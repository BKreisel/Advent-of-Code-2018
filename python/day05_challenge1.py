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


def main():
    polymer = read_input(DAY)[0].rstrip()
    while True:
        polymer, reduced = reduce(polymer)
        if not reduced:
            break
        print(f"\rPolymer Length: {len(polymer)}", end="       ")
    print("")


if __name__ == "__main__":
    main()

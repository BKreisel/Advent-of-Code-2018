from collections import namedtuple
from typing import Dict, Tuple
import re

from util import read_input

DAY = 3

Coordinate = namedtuple("Coordinate", ["x", "y"])


def main():
    claimed_areas: Dict[str, int] = {}
    for line in read_input(DAY):
        start_x, start_y, width, height = parse_claim(line.rstrip())

        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                claimed_areas = add_claim(Coordinate(x, y), claimed_areas)

    overlapping_squares = 0
    for key, value in claimed_areas.items():
        if value > 1:
            overlapping_squares += 1
    print(overlapping_squares)


# Add Claim to Dictionary of Existing Claims
def add_claim(claim: Coordinate, existing_claims: Dict[str, int]) -> Dict[str, int]:
    if str(claim) in existing_claims.keys():
        existing_claims[str(claim)] += 1
    else:
        existing_claims[str(claim)] = 1
    return existing_claims


# Claim line to x, y, width, height
def parse_claim(line: str) -> Tuple[int, int, int, int]:
    CLAIM_RE = r"#(?P<claim>[0-9]+)\s@\s(?P<x>[0-9]+),(?P<y>[0-9]+):\s(?P<height>[0-9]+)x(?P<width>[0-9]+)"
    match = re.match(CLAIM_RE, line)
    if not match:
        raise ValueError(f'Line: "{line}"\nFailed to Parse Claim Input...')
    _, x, y, width, height = match.groups()

    # Coordinates are Distance to Edge + 1
    x = int(x) + 1
    y = int(y) + 1
    return x, y, int(width), int(height)


if __name__ == "__main__":
    main()

from collections import namedtuple
from util import read_input
from typing import List

DAY = 6

Point = namedtuple("Point", ["x", "y"])
MAX_DISTANCE = 10000


def manhattan_distance(c1: Point, c2: Point) -> int:
    return abs(c1.x - c2.x) + abs(c2.y - c1.y)


def main():
    points: List[Point] = []
    for line in read_input(DAY):
        x, y = line.strip().split(", ")
        points.append(Point(int(x), int(y)))

    min_x = min([coord.x for coord in points])
    min_y = min([coord.y for coord in points])
    max_x = max([coord.x for coord in points])
    max_y = max([coord.y for coord in points])

    region_size: int = 0

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            total_distance: int = 0
            for point in points:
                total_distance += manhattan_distance(Point(x, y), point)
            if total_distance < MAX_DISTANCE:
                region_size += 1

    print(region_size)


if __name__ == "__main__":
    main()

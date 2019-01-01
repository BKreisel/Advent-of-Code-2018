from collections import namedtuple
from re import compile
from sys import exit as sysexit

from typing import List
from util import read_input

DAY = 10
UPPER_LIMIT = 25000
Point = namedtuple("Point", ["x", "y"])
Star = namedtuple("Star", ["position", "velocity"])
line_re = compile(r"position=<(?P<x>[-\s\d]+),(?P<y>[-\s\d]+)> velocity=<(?P<vx>[-\s\d]+),(?P<vy>[-\s\d]+)>")


def to_star(line: str) -> Star:
    def to_int(s: str) -> int:
        return int(s.replace(" ", ""))

    match = line_re.match(line.rstrip())
    if not match:
        raise ValueError(f"Unable to Parse Line: {line.rstrip()}")
        sysexit(1)

    groups = match.groupdict()
    velocity = Point(to_int(groups["vx"]), to_int(groups["vy"]))
    x, y = to_int(groups["x"]), to_int(groups["y"])
    return Star(Point(x, y), velocity)


def position(star: Star, time: int = 0) -> Point:
    x = star.position.x + (star.velocity.x * (time + 1))
    y = star.position.y + (star.velocity.y * (time + 1))
    return Point(x, y)


def calculate_area(points: List[Point]) -> int:
    max_x = max([point.x for point in points])
    min_x = min([point.x for point in points])
    max_y = max([point.x for point in points])
    min_y = min([point.x for point in points])
    return (max_x - min_x) * (max_y - min_y)


def print_points(points: List[Point]):
    max_x = max([point.x for point in points])
    min_x = min([point.x for point in points])
    max_y = max([point.y for point in points])
    min_y = min([point.y for point in points])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if len([p for p in points if p.x == x and p.y == y]) > 0:
                print("X", end="")
            else:
                print(" ", end="")
        print("")


def main():
    stars = [to_star(line) for line in read_input(DAY)]
    min_t: int = None
    min_area: int = None

    for t in range(0, UPPER_LIMIT):
        points = [position(star, t) for star in stars]
        area = calculate_area(points)
        if not min_area or area < min_area:
            min_area = area
            min_t = t

    print_points([position(star, min_t) for star in stars])


if __name__ == "__main__":
    main()

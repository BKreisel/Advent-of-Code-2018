from collections import namedtuple
from util import read_input
from typing import List, Union

DAY = 6

Point = namedtuple("Point", ["x", "y"])


def manhattan_distance(c1: Point, c2: Point) -> int:
    return abs(c1.x - c2.x) + abs(c2.y - c1.y)


def shortest_point(grid_point: Point, points: List[Point]) -> Union[Point, None]:
    distances = []
    for point in points:
        distance = manhattan_distance(point, grid_point)
        distances.append((distance, point))
    distances = sorted(distances, key=lambda x: x[0])
    if distances[0][0] == distances[1][0]:
        return None
    return distances[0][1]


def main():
    points: List[Point] = []
    for line in read_input(DAY):
        x, y = line.strip().split(", ")
        points.append(Point(int(x), int(y)))

    min_x = min([coord.x for coord in points])
    min_y = min([coord.y for coord in points])
    max_x = max([coord.x for coord in points])
    max_y = max([coord.y for coord in points])

    distances = {}

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            shortest = shortest_point(Point(x, y), points)
            if not shortest:
                continue
            if shortest in distances.keys():
                distances[shortest] += 1
            else:
                distances[shortest] = 1

    max_area = max([v for v in distances.values()])
    print(max_area)


if __name__ == "__main__":
    main()

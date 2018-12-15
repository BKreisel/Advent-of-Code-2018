from collections import namedtuple
from util import read_input

Node = namedtuple("Node", ["child_count", "metadata"])
DAY = 8


def parse_tree(values):
    child_count = values.pop(0)
    meta_count = values.pop(0)
    nodes = []

    for i in range(child_count):
        values, children = parse_tree(values)
        nodes.extend(children)

    nodes.append(Node(child_count, values[:meta_count]))
    return values[meta_count:], nodes


def main():
    values = [int(x) for x in [x.split() for x in read_input(DAY)][0]]
    _, nodes = parse_tree(values)

    meta_sum = sum([sum(x.metadata) for x in nodes])
    print(f"Metadata Sum: {meta_sum}")


if __name__ == "__main__":
    main()

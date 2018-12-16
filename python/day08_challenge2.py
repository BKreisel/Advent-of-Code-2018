from collections import namedtuple
from util import read_input

Node = namedtuple("Node", ["child_count", "metadata"])
DAY = 8


def parse_tree(data):
    child_count = data.pop(0)
    meta_count = data.pop(0)
    nodes, values = [], []

    for i in range(child_count):
        data, children, value = parse_tree(data)
        values.append(value)
        nodes.extend(children)

    node = Node(child_count, data[:meta_count])
    nodes.append(node)

    if child_count == 0:
        return data[meta_count:], nodes, sum(node.metadata)

    value = 0
    for meta in node.metadata:
        if meta > 0 and meta <= len(values):
            value += values[meta - 1]

    return data[meta_count:], nodes, value


def main():
    data = [int(x) for x in [x.split() for x in read_input(DAY)][0]]
    _, _, root_value = parse_tree(data)

    print(f"Tree Value {root_value}")


if __name__ == "__main__":
    main()

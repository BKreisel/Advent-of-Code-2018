from collections import namedtuple
from util import read_input
from typing import Dict, List

DAY = 7
Requirement = namedtuple("Requirement", ["pre", "post"])


def main():
    requirements = [Requirement(line[5], line[36]) for line in read_input(DAY)]
    steps = set([x.pre for x in requirements] + [x.post for x in requirements])

    dependencies: Dict[str, List[str]] = {}

    for step in steps:
        dependencies[step] = []
    for req in requirements:
        dependencies[req.post].append(req.pre)

    actions: List[str] = []

    while len(actions) < len(steps):
        step = sorted([k for k, v in dependencies.items() if not len(v)])[0]
        actions.append(step)
        dependencies.pop(step, None)

        for req in dependencies.keys():
            dependencies[req] = [x for x in dependencies[req] if x != step]

    print(f"Steps: {''.join(actions)}")


if __name__ == "__main__":
    main()

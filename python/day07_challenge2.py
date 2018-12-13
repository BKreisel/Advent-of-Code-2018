from collections import namedtuple
from util import read_input
from typing import Dict, List, Tuple

DAY = 7
Requirement = namedtuple("Requirement", ["pre", "post"])
WORKERS = 15
STEP_TIME_BASE = 60


def step_time(char: str) -> int:
    return STEP_TIME_BASE + (ord(char) - 64)


def main():
    requirements = [Requirement(line[5], line[36]) for line in read_input(DAY)]
    steps = set([x.pre for x in requirements] + [x.post for x in requirements])
    dependencies: Dict[str, List[str]] = {}

    for step in steps:
        dependencies[step] = []
    for req in requirements:
        dependencies[req.post].append(req.pre)

    actions: List[str] = []
    available_workers: int = WORKERS
    in_progress: List[Tuple[str, int]] = []
    seconds = 0

    while len(actions) < len(steps):
        completed = []
        for idx, action in enumerate(in_progress):
            minutes = action[1] - 1
            step = action[0]

            if minutes == 0:
                actions.append(step)
                completed.append(step)
                available_workers += 1
                for req in dependencies.keys():
                    dependencies[req] = [x for x in dependencies[req] if x != step]
            else:
                in_progress[idx] = (step, minutes)

        in_progress = [x for x in in_progress if x[0] not in completed]

        while available_workers > 0:
            available = sorted([k for k, v in dependencies.items() if not len(v)])
            if len(available):
                step = available[0]
                in_progress.append((step, step_time(step)))
                available_workers -= 1
                dependencies.pop(step)
            else:
                break

        if len(actions) < len(steps):
            seconds += 1

    print(f"Seconds: {seconds}")


if __name__ == "__main__":
    main()

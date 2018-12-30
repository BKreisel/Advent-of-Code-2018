from collections import deque

from util import read_input

DAY = 9


def main():
    data: str = read_input(DAY)[0].split()
    elf_count, last_marble = int(data[0]), int(data[6])
    last_marble *= 100
    circle: deque = deque([0])
    scores: dict = {}

    for marble in range(1, last_marble + 1):
        elf = (marble - 1) % elf_count + 1
        if marble % 23 == 0:
            circle.rotate(7)
            score = circle.pop() + marble
            scores[elf] = scores.get(elf, 0) + score
            circle.rotate(-1)
            continue
        circle.rotate(-1)
        circle.append(marble)
        marble += 1

    high_score = max(scores.values())
    print(high_score)


if __name__ == "__main__":
    main()

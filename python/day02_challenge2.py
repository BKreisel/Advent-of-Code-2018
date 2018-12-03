from util import read_input

DAY = 2


def main():
    box_ids = read_input(DAY)
    for idx1 in range(0, len(box_ids)-1):
        for idx2 in range(idx1+1, len(box_ids)):
            id1 = box_ids[idx1].rstrip()
            id2 = box_ids[idx2].rstrip()
            if compare_ids(id1, id2):
                chars = common_chars(id1, id2)
                print(f"Common Characters: {chars}")


# Find the Common Characters in two box ID's
def common_chars(id1: str, id2: str) -> str:
    chars: list = []
    for idx in range(0, len(id1)):
        if id1[idx] == id2[idx]:
            chars.append(id1[idx])
    return "".join(chars)


# Return True if Box ID's differ by only one character.
def compare_ids(id1: str, id2: str) -> bool:
    deviation = 0
    for idx in range(0, len(id1)):
        if id1[idx] != id2[idx]:
            deviation += 1
        if deviation > 1:
            return False

    return True


if __name__ == "__main__":
    main()

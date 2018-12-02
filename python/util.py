from typing import List

import os.path


# Return Daily Input File as list of strings.
def read_input(day: int) -> List[str]:
    project_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    input_path = os.path.join(project_dir, "input", f"day{day:02}.txt")
    with open(input_path, "r") as file:
        return file.readlines()

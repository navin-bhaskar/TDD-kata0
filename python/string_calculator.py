import re
from typing import List


class StringCalculator:
    """simple string calculator class"""

    def add(self, inp_str: str) -> int:
        acc: int = 0
        numbers: List[int] = []
        if inp_str == "":
            return 0

        split_str: List[str] = re.split(r"[,|\n]", inp_str)
        for num_str in split_str:
            try:
                cur_num: int = int(num_str)
                numbers.append(cur_num)
            except ValueError:
                raise ValueError("Invalid number: {num_str}")

        for num in numbers:
            acc += num

        return acc

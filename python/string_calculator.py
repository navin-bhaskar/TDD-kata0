from typing import List


class StringCalculator:
    """simple string calculator class"""

    def add(self, inp_str: str) -> int:
        acc: int = 0
        if inp_str == "":
            return 0

        try:
            cur_num: int = int(inp_str)
            acc += cur_num
        except ValueError:
            raise ValueError("Invalid number")

        return acc

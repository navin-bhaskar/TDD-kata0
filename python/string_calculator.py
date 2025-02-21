import re
from typing import List


class StringCalculator:

    @staticmethod
    def _get_numbers(inp_str: str, delem: str) -> List[int]:
        reg_exp: str = delem + r"|\n"
        nums_strs: List[str] = re.split(reg_exp, inp_str)

        nums: List[int] = []

        for num_str in nums_strs:
            try:
                nums.append(int(num_str))
            except ValueError:
                raise ValueError(f"Not a valid number {num_str}")
        return nums

    @staticmethod
    def _get_delem(inp_str: str):
        if inp_str.startswith("//"):
            delem: str = inp_str[2]
        else:
            delem = ","
        return delem

    @staticmethod
    def _clean_input(inp_str: str):
        if inp_str.startswith("//"):
            return inp_str[4:]
        return inp_str

    def add(self, inp_str: str) -> int:
        if inp_str == "":
            return 0
        delem = StringCalculator._get_delem(inp_str)
        inp_str = StringCalculator._clean_input(inp_str)
        nums = StringCalculator._get_numbers(inp_str, delem)
        return sum(nums)
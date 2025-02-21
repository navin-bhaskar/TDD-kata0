import re
from typing import List


class StringCalculator:

    @staticmethod
    def _get_numbers(inp_str: str) -> List[int]:
        reg_exp: str = r",|\n"
        nums_strs: List[str] = re.split(reg_exp, inp_str)

        nums: List[int] = []

        for num_str in nums_strs:
            try:
                nums.append(int(num_str))
            except ValueError:
                raise ValueError(f"Not a valid number {num_str}")
            
        return nums


    def add(self, inp_str: str) -> int:
        if inp_str == "":
            return 0
        nums = StringCalculator._get_numbers(inp_str)
        return sum(nums)
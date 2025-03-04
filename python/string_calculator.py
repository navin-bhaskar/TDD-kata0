import re
from typing import List

IGNORE_THRESHOLD_NUM = 1000

class StringCalculator:

    @staticmethod
    def _get_numbers(inp_str: str, delems: List[str]) -> List[int]:
        reg_exp: str = ""
        
        for delem in delems:
            reg_exp += re.escape(delem) + r"|"

        reg_exp += r"\n"

        nums_strs: List[str] = re.split(reg_exp, inp_str)
        nums: List[int] = []

        for num_str in nums_strs:
            try:
                nums.append(int(num_str))
            except ValueError:
                raise ValueError(f"Not a valid number {num_str}")
        return nums

    @staticmethod
    def _get_delems(inp_str: str) -> List[str]:
        delems: List[str] = []
        if inp_str.startswith("//"):
            inp_str = inp_str.removeprefix("//")
            temp: str = inp_str.split("\n")[0]
            bracket_loc: int = temp.find("[")
            if bracket_loc != -1:
                temp_delems = temp.split("]")
                for temp_delem in temp_delems:
                    if temp_delem:
                        delems.append(temp_delem[1:])
            else:
                delems = [temp[0]]
        else:
            delems = [","]
        return delems

    @staticmethod
    def _clean_input(inp_str: str):
        if inp_str.startswith("//"):
            return inp_str.split("\n")[1]
        return inp_str
    
    @staticmethod
    def _check_input(nums: List[int]) -> None:
        neg_numbers = list(filter(lambda num: num < 0, nums))
        if len(neg_numbers) != 0:
            neg_num_str = ", ".join(map(lambda num: str(num), neg_numbers))
            raise ValueError(f"negatives not allowed {neg_num_str}")

    def add(self, inp_str: str) -> int:
        if inp_str == "":
            return 0
        nums: List[int] = []
        delem = StringCalculator._get_delems(inp_str)
        inp_str = StringCalculator._clean_input(inp_str)
        nums = StringCalculator._get_numbers(inp_str, delem)
        self._check_input(nums)
        nums = filter(lambda num: num < IGNORE_THRESHOLD_NUM, nums)
        return sum(nums)
import re
from typing import List, Optional


class StringCalculator:
    """simple string calculator class"""

    @staticmethod
    def _get_numbers(inp_str: str, delimeter: Optional[str] = ",") -> List[int]:
        """Given input string and delimeter, this method attempts to convert them into int
        and return them as a list

        Args:
            inp_str (str): Given delimeter seperated input string
            delimeter (str, optional): . Defaults to ",".

        Raises:
            ValueError: When input contains string that cannot be parsed as int

        Returns:
            List[int]: Numbers found in the input string
        """
        numbers: List[int] = []
        split_str: List[str] = re.split(rf"{re.escape(delimeter)}|\n", inp_str)
        for num_str in split_str:
            try:
                cur_num: int = int(num_str)
                numbers.append(cur_num)
            except ValueError:
                raise ValueError("Invalid number: {num_str}")
        return numbers

    @staticmethod
    def _determine_delimeter(inp_str: str) -> str:
        """Finds and returns the delimeter in input string, if fond

        Args:
            inp_str (str): Input string conating delimeters and numbers

        Returns:
            str: Delemiter as sepcified in input string, defaults to ',' if not found
        """
        if inp_str.startswith("//") and len(inp_str) > 4:
            if inp_str[3] == "\n":  # mandate \n after the delimeter
                return inp_str[2]
        else:
            return ","

    @staticmethod
    def _clean_input(inp_str: str) -> str:
        """Removes the delimeter specifier and delimeter if found, along with the following
        new line.

        Args:
            inp_str (str): Input string conating delimeters and numbers

        Returns:
            str: Cleaned input str
        """
        inp_str = inp_str.strip()
        if inp_str.startswith("//") and len(inp_str) > 4:
            return inp_str[4:]
        return inp_str.strip()

    @staticmethod
    def _check_for_negative_numbers(numbers: List[int]) -> None:
        """Checks if the input numbers has negative numbers and throws
        exception if found. If there are multiple negative numbers then
        they are listed out in exception message (comma seperated)

        Args:
            numbers (List[int]): Numbers extracted from the input string

        Raises:
            ValueError: Raises value error with appropriate message if negative numbers
            are found.
        """
        neg_numbers = list(filter(lambda num: num < 0, numbers))
        if neg_numbers:
            out_str = ",".join(map(lambda num: str(num), neg_numbers))
            raise ValueError("negative numbers not allowed " + out_str)

    def add(self, inp_str: str) -> int:
        if inp_str == "":
            return 0
        delimeter: str = StringCalculator._determine_delimeter(inp_str)
        inp_str: str = StringCalculator._clean_input(inp_str)
        numbers: List[int] = StringCalculator._get_numbers(inp_str, delimeter)
        StringCalculator._check_for_negative_numbers(numbers)
        return sum(numbers)

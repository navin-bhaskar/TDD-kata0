import re
from typing import List

IGNORE_THRESHOLD = 1000


class StringCalculator:
    """simple string calculator class"""

    @staticmethod
    def _get_numbers(inp_str: str, delimeters: List[str]) -> List[int]:
        """Given input string and delimeter, this method attempts to convert them into int
        and return them as a list

        Args:
            inp_str (str): Given delimeter seperated input string
            delimeters (str, optional): A list of delimeters that were found in input

        Raises:
            ValueError: When input contains string that cannot be parsed as int

        Returns:
            List[int]: Numbers found in the input string
        """
        numbers: List[int] = []
        re_del = r""
        for delem in delimeters:
            re_del = re_del + rf"{re.escape(delem)}|"

        re_del = re_del + r"\n"

        split_str: List[str] = re.split(re_del, inp_str)
        for num_str in split_str:
            try:
                cur_num: int = int(num_str)
                numbers.append(cur_num)
            except ValueError:
                raise ValueError("Invalid number: {num_str}")
        return numbers

    @staticmethod
    def _determine_delimeters(inp_str: str) -> List[str]:
        """Finds and returns the delimeter in input string, if fond

        Args:
            inp_str (str): Input string conating delimeters and numbers

        Returns:
            str: Delemiter as sepcified in input string, defaults to ',' if not found
        """
        if inp_str.startswith("//") and len(inp_str) > 4:
            new_line_at = inp_str.find("\n")
            if new_line_at == -1:
                raise ValueError("Invalid input")
            delems = inp_str[2:new_line_at]
            all_delems = []
            if delems.find("[") == -1:
                # Single char delemeter
                all_delems.append(delems)
            else:
                # Multi char/Multi dlemes
                for cur_del in delems.split("]"):
                    if not cur_del:
                        continue  # Ignore the last empty string after split
                    all_delems.append(cur_del[1:])  # Ignore leading [
            return all_delems
        else:
            return [","]

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
        if inp_str.startswith("//"):
            new_line_at = inp_str.find("\n")
            # jumpover all delimeters
            inp_str = inp_str[new_line_at + 1 :]
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
        delimeters: str = StringCalculator._determine_delimeters(inp_str)
        inp_str: str = StringCalculator._clean_input(inp_str)
        numbers: List[int] = StringCalculator._get_numbers(inp_str, delimeters)
        StringCalculator._check_for_negative_numbers(numbers)
        # filter out numbers that are greater than IGNORE_THRESHOLD
        numbers = filter(lambda num: num < IGNORE_THRESHOLD, numbers)
        return sum(numbers)

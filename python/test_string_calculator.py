import unittest

from string_calculator import StringCalculator


class TestStringCalc(unittest.TestCase):
    
    def test__add_given_comma_seperated_num_str__returns_sum(self):
        """ req1: The method can take up to two numbers, separated by commas, and will return their sum.
        for example “” or “1” or “1,2” as inputs.
        (for an empty string it will return 0)"""
        sc = StringCalculator()
        res = sc.add("")
        assert res == 0

        res = sc.add("1")
        assert res == 1

        res = sc.add("1,2")
        assert res == 3

    def test__add_takes_in_arbitrary_numbers__sum_of_those_numbers_returned(self):
        """req2: Allow the Add method to handle an unknown amount of numbers"""
        sc = StringCalculator()

        inp_str: str = ""
        for n in range(1, 11):
            expected_sum = (n * (n+1)) // 2
            inp_str += str(n)
            assert sc.add(inp_str) == expected_sum
            inp_str += ","


    def test__newline_in_input__newline_considered_as_seperator(self):
        """req3:  Allow the Add method to handle new lines between numbers (instead of commas).
            1. the following input is ok: “1\n2,3” (will equal 6)
            2. the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)"""
        sc = StringCalculator()
        assert sc.add("1\n2,3") == 6
        

    def test__custom_delimeter_passed__custom_delimeter_used(self):
        """req 4. Support different delimiters
        to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
        the first line is optional. all existing scenarios should still be supported"""
        sc = StringCalculator()

        assert sc.add("//;\n1;2") == 3

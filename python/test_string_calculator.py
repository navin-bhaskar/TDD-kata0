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



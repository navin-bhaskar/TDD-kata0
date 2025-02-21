import unittest

from string_calculator import StringCalculator


class TestStringCalc(unittest.TestCase):
    
    def test__add_given_comma_seperated_num_str__returns_sum(self):
        """ The method can take up to two numbers, separated by commas, and will return their sum.
        for example “” or “1” or “1,2” as inputs.
        (for an empty string it will return 0)"""
        sc = StringCalculator()
        res = sc.add("")
        assert res == 0

        res = sc.add("1")
        assert res == 1
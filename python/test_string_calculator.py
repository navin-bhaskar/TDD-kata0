import unittest

from string_calculator import StringCalculator


class StringCalcTester(unittest.TestCase):

    def test_pass_empty_string_to_add__get_back_0(self):
        sc = StringCalculator()
        assert sc.add("") == 0

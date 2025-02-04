import unittest

from string_calculator import StringCalculator


class StringCalcTester(unittest.TestCase):

    def test_pass_empty_string_to_add__get_back_0(self):
        sc = StringCalculator()
        assert sc.add("") == 0

    def test_input_single_digit_str__get_back_same_digit_as_int(self):
        sc = StringCalculator()
        out = sc.add("1")
        assert isinstance(out, int)
        assert out == 1

    def test_pass_comma_seperated_ints__add_returns_sum_of_ints(self):
        sc = StringCalculator()
        assert sc.add("1,5") == 6

        inp_str: str = ""
        for n in range(1, 11):
            expected_sum = n * (n + 1) // 2
            inp_str = inp_str + str(n)
            assert sc.add(inp_str) == expected_sum
            inp_str = inp_str + ","

    def test_input_has_new_line__new_line_also_handled_as_seperator(self):
        sc = StringCalculator()

        assert sc.add("1\n2,3") == 6

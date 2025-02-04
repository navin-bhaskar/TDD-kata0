import unittest

from string_calculator import StringCalculator


class TestStringCalc(unittest.TestCase):

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

    def test_add_input_has_new_line__new_line_also_handled_as_seperator(self):
        sc = StringCalculator()

        assert sc.add("1\n2,3") == 6

    def test_add_input_has_custom_delimeter__custom_delimeter_is_used(self):
        sc = StringCalculator()
        assert sc.add("//;\n1;2") == 3

    def test_input_string_has_negative_numbers__add_throws_excpetion_with_message(self):
        sc = StringCalculator()
        with self.assertRaises(ValueError) as context:
            sc.add("1,-1")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1")

    def test_input_string_has_multiple_negative_numbers__all_negative_numbers_listed(
        self,
    ):
        sc = StringCalculator()
        with self.assertRaises(ValueError) as context:
            sc.add("1,-1,2,3,-4,5,-6,-8,9")
        self.assertEqual(
            str(context.exception), "negative numbers not allowed -1,-4,-6,-8"
        )

    def test_input_has_numbers_greater_than_1000__numbers_greater_than_1000_ignored(
        self,
    ):
        sc = StringCalculator()
        assert sc.add("1\n2,1000,1001,3") == 6

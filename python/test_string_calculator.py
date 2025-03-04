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
        """req 4: Support different delimiters
        to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
        the first line is optional. all existing scenarios should still be supported"""
        sc = StringCalculator()

        assert sc.add("//;\n1;2") == 3

    def test__negative_numers_in_input_to_add__throws_exception(self):
        """req5: 5. Calling Add with a negative number will throw an exception 
        “negatives not allowed” - and the negative that was passed.
        if there are multiple negatives, show all of them in the exception message."""
        sc = StringCalculator()

        with self.assertRaises(ValueError) as cm:
            sc.add("1,2,-3,4,5,-6")

        self.assertEqual("negatives not allowed -3, -6", str(cm.exception))

    def test__nums_greater_than_1000_passed__numbers_greater_than_thousand_ignored(self):
        """req6: Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2"""
        sc = StringCalculator()

        self.assertEqual(sc.add("1,2,1000,1001,3"), 6)

    def test__varibale_length_delimter_passed__variable_length_delimter_used(self):
        """req7: Delimiters can be of any length with the following format: 
        “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6"""
        sc = StringCalculator()

        self.assertEqual(sc.add("//[***]\n1***2***3"), 6)

    def test__multiple_delimter_passed__multiple_delimters_considered(self):
        """ Allow multiple delimiters like this: “//[delim1][delim2]\n” 
        for example “//[\*][%]\n1\*2%3” should return 6."""
        sc = StringCalculator()
        
        self.assertEqual(sc.add("//[\*][%]\n1\*2%3"), 6)

    def test__multiple_delimter_longer_than_one_char_passed__multiple_delimters_considered(self):
        """ Allow multiple delimiters like this: “//[delim1][delim2]\n” 
        for example “//[\*][%]\n1\*2%3” should return 6."""
        sc = StringCalculator()
        
        self.assertEqual(sc.add("//[,][%][^^]\n1,2%3^^4"), 10)


import unittest
from numbers_to_words import replace_numbers_with_words

class TestNumbersToWords(unittest.TestCase):
    test_values = [
        {"actual": "1 2 3 the number is capitalized", "expected": "One two three the number is capitalized"},
        {"actual": "Here 57 is a double digit", "expected": "Here fifty-seven is a double digit"},
        {"actual": "There are no numbers in this string", "expected": "There are no numbers in this string"},
        # test empty string
        {"actual": "", "expected": ""},
    ]

    number_too_long_str = "The value 999 is too long for the function to parse"

    def test_numbers_to_words(self):
        for test_value in self.test_values:
            self.assertEqual(replace_numbers_with_words(test_value['actual']), test_value['expected'])

    def test_assert_raise(self):
        with self.assertRaises(ValueError):
            replace_numbers_with_words(self.number_too_long_str)
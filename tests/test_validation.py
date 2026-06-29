import unittest

from num_to_language.validation import (
    validate_number,
    is_decimal_number,
    contains_only_digits,
    within_max_length,
    remove_leading_zeros
)

class ValidationTests(unittest.TestCase):

    def test_validate_number_valid(self):
        self.assertEqual(validate_number("123"), "123")

    def test_validate_number_removes_leading_zeros(self):
        self.assertEqual(validate_number("000123"), "123")

    def test_validate_number_zero(self):
        self.assertEqual(validate_number("0000"), "0")

    def test_validate_number_too_long(self):
        with self.assertRaises(ValueError):
            validate_number("1000000000000")

    def test_validate_number_letters(self):
        with self.assertRaises(ValueError):
            validate_number("12a3")

    def test_validate_number_empty(self):
        with self.assertRaises(ValueError):
            validate_number("")

    def test_contains_only_digits_with_valid_digits(self):
        self.assertTrue(contains_only_digits("123"))

    def test_contains_only_digits_with_letters(self):
        self.assertFalse(contains_only_digits("12a3"))

    def test_contains_only_digits_with_negative_sign(self):
        self.assertFalse(contains_only_digits("-123"))

    def test_contains_only_digits_with_decimal_point(self):
        self.assertFalse(contains_only_digits("12.3"))

    def test_contains_only_digits_with_empty_string(self):
        self.assertFalse(contains_only_digits(""))

    def test_within_max_length_with_twelve_digits(self):
        self.assertTrue(within_max_length("999999999999"))

    def test_within_max_length_with_thirteen_digits(self):
        self.assertFalse(within_max_length("1000000000000"))

    def test_remove_leading_zeros_from_number(self):
        self.assertEqual(remove_leading_zeros("000123"), "123")

    def test_remove_leading_zeros_from_zero(self):
        self.assertEqual(remove_leading_zeros("0"), "0")

    def test_remove_leading_zeros_from_all_zeros(self):
        self.assertEqual(remove_leading_zeros("0000"), "0")

    def test_is_decimal_number_with_valid_number(self):
        self.assertTrue(is_decimal_number("123"))

    def test_is_decimal_number_with_zero(self):
        self.assertTrue(is_decimal_number("0"))

    def test_is_decimal_number_with_leading_zeros(self):
        self.assertTrue(is_decimal_number("000123"))

    def test_is_decimal_number_with_letters(self):
        self.assertFalse(is_decimal_number("abc"))

    def test_is_decimal_number_with_too_many_digits(self):
        self.assertFalse(is_decimal_number("1000000000000"))


if __name__ == "__main__":
    unittest.main()
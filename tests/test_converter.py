import unittest

from num_to_language.converter import (
    num_to_language,
    split_into_groups,
    convert_group,
)


class ConverterTests(unittest.TestCase):

    def test_num_to_language_zero(self):
        self.assertEqual(num_to_language("0"), "zero")

    def test_num_to_language_single_digit(self):
        self.assertEqual(num_to_language("7"), "seven")

    def test_num_to_language_teens(self):
        self.assertEqual(num_to_language("13"), "thirteen")

    def test_num_to_language_tens_exact(self):
        self.assertEqual(num_to_language("40"), "forty")

    def test_num_to_language_tens_with_ones(self):
        self.assertEqual(num_to_language("42"), "forty-two")

    def test_num_to_language_hundreds_exact(self):
        self.assertEqual(num_to_language("100"), "one hundred")

    def test_num_to_language_hundreds_with_ones(self):
        self.assertEqual(num_to_language("101"), "one hundred one")

    def test_num_to_language_hundreds_with_teens(self):
        self.assertEqual(num_to_language("115"), "one hundred fifteen")

    def test_num_to_language_hundreds_with_tens(self):
        self.assertEqual(num_to_language("123"), "one hundred twenty-three")

    def test_num_to_language_thousand_exact(self):
        self.assertEqual(num_to_language("1000"), "one thousand")

    def test_num_to_language_thousand_with_remainder(self):
        self.assertEqual(num_to_language("1001"), "one thousand one")

    def test_num_to_language_complex_thousands(self):
        self.assertEqual(
            num_to_language("123456"),
            "one hundred twenty-three thousand four hundred fifty-six",
        )

    def test_num_to_language_millions(self):
        self.assertEqual(
            num_to_language("123456789"),
            "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine",
        )

    def test_num_to_language_billions(self):
        self.assertEqual(
            num_to_language("123456789012"),
            "one hundred twenty-three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve",
        )

    def test_num_to_language_max_value(self):
        self.assertEqual(
            num_to_language("999999999999"),
            "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine",
        )

    def test_num_to_language_leading_zeros(self):
        self.assertEqual(num_to_language("000123"), "one hundred twenty-three")

    def test_num_to_language_invalid_letters(self):
        with self.assertRaises(ValueError):
            num_to_language("12a3")

    def test_num_to_language_too_large(self):
        with self.assertRaises(ValueError):
            num_to_language("1000000000000")

    def test_split_into_groups_single_group(self):
        self.assertEqual(split_into_groups("123"), ["123"])

    def test_split_into_groups_two_groups(self):
        self.assertEqual(split_into_groups("1234"), ["1", "234"])

    def test_split_into_groups_four_groups(self):
        self.assertEqual(split_into_groups("123456789012"), ["123", "456", "789", "012"])

    def test_convert_group_zero(self):
        self.assertEqual(convert_group("000"), "")

    def test_convert_group_single_digit(self):
        self.assertEqual(convert_group("007"), "seven")

    def test_convert_group_tens(self):
        self.assertEqual(convert_group("042"), "forty-two")

    def test_convert_group_hundreds(self):
        self.assertEqual(convert_group("123"), "one hundred twenty-three")


if __name__ == "__main__":
    unittest.main()
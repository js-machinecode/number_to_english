from num_to_language.type_defs import DecimalString

MAX_DIGITS = 12


def validate_number(value: DecimalString) -> DecimalString:
    """
    Validate and normalize a decimal number string.

    Returns the cleaned number string.
    Raises ValueError if the input is invalid.
    """
    if not is_decimal_number(value):
        raise ValueError("Input must be a decimal number between 0 and 999,999,999,999.")

    return remove_leading_zeros(value)


def is_decimal_number(value: DecimalString) -> bool:
    """
    Return True if value is a valid decimal number string.
    """
    return contains_only_digits(value) and within_max_length(value)


def contains_only_digits(value: DecimalString) -> bool:
    """
    Return True if value is non-empty and contains only digits.
    """
    return value.isdigit()


def within_max_length(value: DecimalString) -> bool:
    """
    Return True if value is no more than 12 digits long.
    """
    return len(value) <= MAX_DIGITS


def remove_leading_zeros(value: DecimalString) -> DecimalString:
    """
    Remove leading zeros while preserving one zero if the value is all zeros.
    """
    cleaned = value.lstrip("0")

    if cleaned == "":
        return "0"

    return cleaned
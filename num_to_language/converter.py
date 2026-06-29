from num_to_language.constants import (
    ONES,
    TENS,
    HUNDRED,
    SCALES,
)
from num_to_language.type_defs import (
    DecimalString,
    EnglishNumber,
)
from num_to_language.validation import validate_number


def num_to_language(value: DecimalString) -> EnglishNumber:
    """
    Convert a validated decimal number string into English words.
    """

    value = validate_number(value)

    if value == "0":
        return ONES[0]

    groups = split_into_groups(value)

    words = []

    total_groups = len(groups)

    for index, group in enumerate(groups):

        group_words = convert_group(group)

        if not group_words:
            continue

        scale = SCALES[total_groups - index - 1]

        if scale:
            words.append(f"{group_words} {scale}")
        else:
            words.append(group_words)

    return " ".join(words)


def split_into_groups(value: DecimalString) -> list[DecimalString]:
    """
    Split a decimal string into groups of three digits.

    Example:
        "123456789" ->
        ["123", "456", "789"]
    """

    groups = []

    while value:
        groups.insert(0, value[-3:])
        value = value[:-3]

    return groups


def convert_group(value: DecimalString) -> EnglishNumber:
    """
    Convert a three-digit decimal string (000-999)
    into its English-language representation.
    """

    # Always work with exactly three digits.
    value = value.zfill(3)

    hundreds_digit = value[0]
    tens_digit = value[1]
    ones_digit = value[2]

    words = []

    # --------------------
    # Hundreds
    # --------------------

    if hundreds_digit != "0":
        words.append(ONES[int(hundreds_digit)])
        words.append(HUNDRED)

    # --------------------
    # Tens / Ones
    # --------------------

    last_two_digits = value[1:]

    # 00
    if last_two_digits == "00":
        return " ".join(words)

    # 01 - 19
    if last_two_digits[0] == "0":
        words.append(ONES[int(last_two_digits[1])])

    elif last_two_digits[0] == "1":
        words.append(ONES[int(last_two_digits)])

    # 20 - 99
    else:

        tens_word = TENS[int(last_two_digits[0]) * 10]

        if last_two_digits[1] == "0":
            words.append(tens_word)
        else:
            ones_word = ONES[int(last_two_digits[1])]
            words.append(f"{tens_word}-{ones_word}")

    return " ".join(words)
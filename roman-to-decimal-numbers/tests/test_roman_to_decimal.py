import pytest

from roman_to_decimal import roman_to_decimal

MAPPINGS: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


@pytest.mark.parametrize("test_input,expected", MAPPINGS.items())
def test_standard_numbers(test_input, expected):
    assert roman_to_decimal(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("IX", 9), ("IV", 4)])
def test_number_with_substraction(test_input, expected):
    assert roman_to_decimal(test_input) == expected


def test_largest_number():
    assert roman_to_decimal("MMMCMXCIX") == 3_999


@pytest.mark.parametrize("test_input,expected", [("IX", 9), ("ix", 9)])
def test_accepts_different_chars_cases(test_input, expected):
    assert roman_to_decimal(test_input) == expected


def test_raises_exception_with_empty_string():
    with pytest.raises(ValueError):
        roman_to_decimal("")


def test_raises_exception_with_first_character_invalid():
    """This specific case has to be tested because we always try to map the first character
    before we start inspecting the rest of the string
    """
    with pytest.raises(KeyError):
        roman_to_decimal("P")


@pytest.mark.parametrize("test_input", ["P", "IP", "ASD"])
def test_raises_exception_with_invalid_characters(test_input):
    with pytest.raises(KeyError):
        roman_to_decimal(test_input)

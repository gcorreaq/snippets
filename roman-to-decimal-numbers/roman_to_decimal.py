MAPPINGS: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def roman_to_decimal(roman_numeral: str) -> int:
    """Transforms a roman numeral into its decimal representation

    Empty strings or invalid characters will raise exceptions.

    Note that the biggest number that can be transformed is MMMCMXCIX (3999). For
    more details see https://en.wikipedia.org/wiki/Roman_numerals#Standard_form
    """

    if len(roman_numeral) < 1:
        raise ValueError("Value can't be empty")

    # With upper() we make sure the letters will always be uppercase, to match the keys in our
    # MAPPINGS dictionary
    roman_numeral = roman_numeral.upper()

    # We will keep the total accumulated number here
    result = 0
    # To make things easier, we start with the value of the first character
    # for the operations below
    previous_value = MAPPINGS[roman_numeral[0]]

    # Here the use of enumerate() is just for having nice exception messages
    for position, character in enumerate(roman_numeral, start=1):
        try:
            current_value = MAPPINGS[character]
        except KeyError as e:
            raise KeyError(
                f"Character {character} at position {position} is not supported or is invalid"
            ) from e

        # If the value of the previous character is greater or the same as the current one,
        # we just add them
        if previous_value >= current_value:
            result += current_value
        else:
            # Here we apply the following operation that considers reverting the addition
            # of the previous value, and then correctly using the previous value to substract
            # it from the current value
            #
            #  result = (result - previous_value) + (current_value - previous_value)
            #
            # That is equivalent to the expression below
            result += current_value - (2 * previous_value)

        previous_value = current_value

    return result


if __name__ == "__main__":
    roman_numeral = input("Roman numeral: ")
    decimal_number = roman_to_decimal(roman_numeral)
    print(f"Decimal number: {decimal_number}")

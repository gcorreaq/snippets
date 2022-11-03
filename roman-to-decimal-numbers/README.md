# Transform roman numbers to decimal

[README en español](README.es.md)

The code was initially created as a solution for a problem for the Programming class at the Universidad Técnica Federico Santa María (UTFSM or USM) when I was a teacher assistant. I originally posted the code in Github Gists but I never updated it, and people have already commented about some issues with it. Over time I will update the code so it's back to work with modern Python versions.

There's two scripts:

- [`roman_to_decimal.py`](roman_to_decimal.py): The code updated to run in modern Python versions
- [`romano_a_decimal.py`](romano_a_decimal.py): The same code but with comments in Spanish, explaining every single bit of the code

Both only support transforming numbers up to 3999 (See <https://en.wikipedia.org/wiki/Roman_numerals#Standard_form>)

For any questions, comments or feedback, please check the [issues list](https://github.com/gcorreaq/snippets/issues), and if you cannot find something similar, please [add a new issue](https://github.com/gcorreaq/snippets/issues/new) in the project.

## Explanation of the algorithm

The main idea behind this code is the following:

- To transform roman numerals to decimal numbers we need to consider that roman numerals are represented by a chain of characters, and the decimal representation of the whole roman number is a combination of adding or substracting the value of each character to a running total.
- We need to inspect the roman numeral character by character, and what we do with each character depends on the decimal representation of the previous character. This can also be done in reverse: we inspect a character, and what we do with its decimal representation depends on the decimal value of the next character.
- At the end we take the running total and we use that as our decimal representation

""" Task 5
Author: Andrii Malchyk
v.1.0
"""

import string


def count_letters(input_string):
    letters_dictionary = {}
    for char in string.ascii_lowercase:
        count = input_string.count(char)
        if count != 0:
            letters_dictionary.update({char: count})
    return letters_dictionary

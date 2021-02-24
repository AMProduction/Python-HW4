""" Task 4
Author: Andrii Malchyk
v.1.0
"""

import string


def in_all_strings(*input_strings):
    chars_set = set()
    flag = 0
    for char in string.ascii_lowercase:
        for word in input_strings:
            if word.count(char) > 0:
                flag += 1
        if flag == len(input_strings):
            chars_set.add(char)
        flag = 0
    return chars_set


def in_one_string(*input_strings):
    chars_set = set()
    flag = 0
    for char in string.ascii_lowercase:
        for word in input_strings:
            if word.count(char) > 0:
                flag += 1
        if flag != 0:
            chars_set.add(char)
        flag = 0
    return chars_set


def not_used_string(*input_strings):
    chars_set = set()
    flag = 0
    for char in string.ascii_lowercase:
        for word in input_strings:
            if word.count(char) == 0:
                flag += 1
        if flag == len(input_strings):
            chars_set.add(char)
        flag = 0
    return chars_set


def in_two_strings(*input_strings):
    chars_set = set()
    flag = 0
    for char in string.ascii_lowercase:
        for word in input_strings:
            if word.count(char) > 0:
                flag += 1
                if flag == 2:
                    chars_set.add(char)
                    flag = 0
                    break
        flag = 0
    return chars_set


print(in_all_strings("hello", "world", "python"))
print(in_one_string("hello", "world", "python"))
print(not_used_string("hello", "world", "python"))
print(in_two_strings("hello", "world", "python"))

""" Task 2
Author: Andrii Malchyk
v.1.0
"""


def IsPalindrom(palin):
    palin = palin.lower()
    string_forward = ""
    for char in palin:
        if char.isalpha():
            string_forward += char
    string_reverse = string_forward[::-1]
    if string_forward == string_reverse:
        return True
    else:
        return False


print("Please, enter a string: ")
input_string = input()
print(IsPalindrom(input_string))

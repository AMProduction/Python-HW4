""" Task 3
Author: Andrii Malchyk
v.1.0
"""


def word_len(word):
    return len(word)


def get_shortest_word(input_string):
    words_list = input_string.split(" ")
    words_list.sort(key=word_len)
    return words_list[0]


print("Please, enter a string: ")
input_string = input()
print(get_shortest_word(input_string))

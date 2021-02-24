""" Task 1
Author: Andrii Malchyk
v.1.0
"""

print("Please, enter a string: ")
input_string = input()
output_string = ""
for char in input_string:
    if char == "\'":
        char = char.replace("\'", "\"")
        output_string += char
    elif char == "\"":
        char = char.replace("\"", "\'")
        output_string += char
    else:
        output_string += char
print(output_string)

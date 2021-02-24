# Python Homework 4
## Python Strings
### Task 1
Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.
### Task 2
Write a function that check whether a string is a palindrome or not. To check your implementation you can use strings from here (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)
### Task 3
Implement a function `get_shortest_word(s: str) -> str` which returns the shortest word in the given string. The word can contain any symbols except whitespaces (` `, `\n`, `\t`
and so on). If there are multiple shortest words in the string with a same length return the word that occurs first. Usage of any split functions is forbidden.  
Example:
```python
>>> get_shortest_word('Python is simple and effective!')
'is'
>>> get_shortest_word('Any pythonista like namespaces a lot, a? O')
'a'
```
### Task 4
Implement a bunch of functions which receive a changeable number of strings and return next parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string  

*Note: use `string.ascii_lowercase` for list of alphabet letters*
```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```
### Task 5
Implement a function, that takes string as an argument and returns a dictionary, that contains letters of given string as keys and a number of their occurrence as values.
```python
print(count_letters("stringsample"))
>>> {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}
```

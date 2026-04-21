# string methods 
# String methods are built-in functions that allow you to manipulate and work with strings in Python.
text = 'I am learning Python string methods.'

# 1. upper() - Converts all characters to uppercase
result = text.upper() # OUTPUT: 'I AM LEARNING PYTHON STRING METHODS.'

# 2. lower() - Converts all characters to lowercase
result = text.lower() # OUTPUT: 'i am learning python string methods.'

# 3. title() - Converts the first character of each word to uppercase
result = text.title() # OUTPUT: 'I Am Learning Python String Methods.'

# 4. strip() - Removes leading and trailing whitespace
text_with_spaces = '   Hello, World!   '
result = text_with_spaces.strip() # OUTPUT: 'Hello, World!'

# 5. replace() - Replaces a specified substring with another substring
result = text.replace('Python', 'JavaScript') # OUTPUT: 'I am learning JavaScript string methods.'

# 6. split() - Splits the string into a list of substrings based on a specified delimiter
result = text.split() # OUTPUT: ['I', 'am', 'learning', 'Python', 'string', 'methods.']

# 7. isalpha() - Checks if all characters in the string are alphabetic
result = text.isalpha() # OUTPUT: False (because of spaces and punctuation)

# 8. find() - Returns the index of the first occurrence of a specified substring
result = text.find('Python') # OUTPUT: 14 (index of the first character of 'Python')
result = text.find('Java') # OUTPUT: -1 (because 'Java' is not found in the string)

# 9. count() - Returns the number of occurrences of a specified substring
result = text.count('a') # OUTPUT: 2 (number of times 'a' appears in the string)

# 10. startswith() - Checks if the string starts with a specified substring
result = text.startswith('I am') # OUTPUT: True (because the string starts with 'I am')

# 11. endswith() - Checks if the string ends with a specified substring
result = text.endswith('methods.') # OUTPUT: True (because the string ends with 'methods.')

# 12. len() - Returns the length of the string
result = len(text) # OUTPUT: 38 (number of characters in the string, including spaces and punctuation)

# 13. format() - Formats the string using placeholders
name = 'Alice'
age = 30
result = "My name is {} and I am {} years old.".format(name, age) # OUTPUT: 'My name is Alice and I am 30 years old.'

# 14. isdigit() - Checks if all characters in the string are digits
number_string = '12345'
result = number_string.isdigit() # OUTPUT: True (because all characters are digits)



        

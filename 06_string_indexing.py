# STRING INDEXING & SLICING
# String indexing allows you to access individual characters in a string using their position (index).
# In Python, indexing starts from 0.

text = "I am learning Python"

# 1. Indexing (positive index)
result = text[0]   # OUTPUT: 'I'  (first character)
result = text[3]   # OUTPUT: 'm'  (index 3 character)
result = text[5]   # OUTPUT: 'l'

# 2. Negative indexing (starts from the end)
result = text[-1]   # OUTPUT: 'n'  (last character)
result = text[-2]   # OUTPUT: 'o'
result = text[-6]   # OUTPUT: 'P'

# 3. Slicing (start:end)
# NOTE: end index is NOT included
result = text[0:4]   # OUTPUT: 'I am'
result = text[5:13]  # OUTPUT: 'learning'
result = text[14:20] # OUTPUT: 'Python'

# 4. Slicing with step (start:end:step)
result = text[0:20:2]   # OUTPUT: every 2nd character
result = text[::2]      # OUTPUT: full string with step 2
result = text[::1]      # OUTPUT: original string

# 5. Reverse string using slicing
result = text[::-1]  # OUTPUT: 'nohtyP gninrael ma I'

# 6. Omitting start index
result = text[:4]    # OUTPUT: 'I am' (from start to index 4)

# 7. Omitting end index
result = text[5:]    # OUTPUT: 'learning Python'

# 8. String length with indexing relation
length = len(text)   # OUTPUT: total number of characters
last_char = text[length - 1]  # same as text[-1]

# 9. Strings are IMMUTABLE (cannot change by index)
# text[0] = "A"  ERROR (not allowed)

# 10. Practical example
word = "Python"
first_letter = word[0]   # 'P'
last_letter = word[-1]   # 'n'
middle = word[1:5]       # 'ytho'
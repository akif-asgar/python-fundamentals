# for is a loop that iterates over a sequence (like list, tuple, string) or other iterable objects (like range)
# for use with range function to create a sequence of numbers
# 1.                 range (start, stop, step)
# 2.                 start: the value of the first number in the sequence (default is 0)
# 3.                 stop: the value at which the sequence will stop (not included in the sequence)
# 4.                 step: the difference between each number in the sequence (default is 1)

for i in range(5):  # will print numbers from 0 to 4
    print(i)


for i in range(1, 10, 2):  # will print odd numbers from 1 to 9
    
    print(i)

for i in range(10, 0, -1):  # will print numbers from 10 to 1 in reverse order
    print(i)
    
for i in range(0, 11):
    
    print(i, end=" ")  # will print numbers from 0 to 10 on the same line with space in between
# for loop with strings

word = "Python"

for letter in word:  # will print each letter in the word "Python"
    print(letter)
    

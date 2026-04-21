# 1.task_01---> check input and if there are spaces change them to - 
# 2.task_02---> check input and if there is not uppercase output " Uppercase letter is missing"
# 3.task_03---> check input If the first and last letters of the word are the same. If they are the same, output "The first and last letters are the same". Otherwise, output "The first and last letters are different".
# 4.task_04 ---> check input and:
# print the middle character of the word using indexing
# if the word length is even, print "No middle character"


# Task 1
user_input = input("Enter your text: ")

if " " in user_input:
    
    result = user_input.replace(" ", "-")
 
# Task 2

if user_input == user_input.lower():
    
    print('Uppercase letter is missing')

# Task 3

if len(user_input) > 0:
    if user_input[0] == user_input[-1]:
        print("The first and last letters are the same")

# Task 4

if len(user_input) > 0:

    if len(user_input) % 2 == 1:
        middle_index = len(user_input) // 2
        print(user_input[middle_index])
    else:
        print("No middle character") 
 


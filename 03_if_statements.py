# we can use if statement to make decision in our code
# if statement is a conditional statement that allows us to execute a block of code only if a certain condition is true


age = int(input("Enter your age: ")) # input function is used to get input from the user


if age < 18:
    
    print(" You must be 18 or older to login to the web site.")
    
elif  age > 200: # we can use elif to check multiple conditions
    
    print(" invalid age. Please enter a valid age.")
    
    
else:  # if the age is between 18 and 200, we can allow the user to login
      
    print(" You can login to the web site.")
    
    
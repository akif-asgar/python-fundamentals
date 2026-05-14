# functions are reusable pieces of code that perform a specific task. 
#              They allow us to break our code into smaller, more manageable chunks, 
#              and they can be called multiple times throughout our program.

# return is a keyword that allows a function to send a value back to the caller.

def add_numbers(num1, num2):
    """This function takes two numbers and returns their sum."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """This function takes two numbers and returns their difference."""
    return num1 - num2

def multiply_numbers(num1, num2):
    
    """This function takes two numbers and returns their product."""
    return num1 * num2  

def divide_numbers(num1, num2):
    """This function takes two numbers and returns their quotient."""
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2  


def greet(name):
    """This function takes a name and returns a greeting message."""
    return f"Hello, {name}! Welcome to the world of functions."


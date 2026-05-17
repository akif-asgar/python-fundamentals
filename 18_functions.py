# functions are reusable pieces of code that perform a specific task. 
#              They allow us to break our code into smaller, more manageable chunks, 
#              and they can be called multiple times throughout our program.

# return is a keyword that allows a function to send a value back to the caller.


# 1. positional arguments: 
# These are the most common type of arguments. 
# They are passed to a function in the order they are defined.

def add_numbers(num1, num2):
    return num1 + num2

def greet(name):
    return f"Hello, {name}! Welcome to the world of functions."

# 2. default arguments:
# These are arguments that have a default value. 
# If the caller does not provide a value for a default argument,

def greet(name,surname, subject = "Hi, how are you?"):
    return f"Hello, {name} {surname}! {subject}"

# 3. keyword arguments:
# These are arguments that are passed to a function using their parameter names.

def get_phone_number(country_code, area_code, phone_number):
    return f"+{country_code} ({area_code}) {phone_number}"

print(get_phone_number(country_code="1", area_code="123", phone_number="4567890"))


#4. arbitrary arguments:
# These are arguments that allow a function to accept an arbitrary number of arguments.

#4.1 *args: This allows a function to accept any number of positional arguments.

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))

#4.2 **kwargs: This allows a function to accept any number of keyword arguments.
def contact_info(name, **kwargs):
    info = f"Name: {name}\n"
    for key, value in kwargs.items():
        info += f"{key.capitalize()}: {value}\n"
    return info

print(contact_info("Alice", email="alice@example.com", phone="123-456-7890"))


# Combining *args and **kwargs in a function allows you to create flexible functions that can handle a wide range of input.
def worker_info (*args, **kwargs):
    
    info = "Worker Information:\n"
    for arg in args:
        info += f"{arg}\n"
    for key, value in kwargs.items():
        info += f"{key.capitalize()}: {value}\n"
    return info
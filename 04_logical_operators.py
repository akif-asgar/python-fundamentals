# logical operators are used to combine multiple conditions in our code
# there are three logical operators in python: and, or, not
# or  -- one of the conditions must be true
# and -- both conditions must be true
# not -- negates the condition


username = "admin"
password = "1234"

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if input_username == username and input_password == password:
    print("Login successful")

if input_username == username or input_password == password:
    print("Partial match")

if not input_username == "guest":
    print("Not a guest user")


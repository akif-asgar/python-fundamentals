"""
While Loops in Python
---------------------
A while loop runs as long as a condition is True.
"""

# 1. Empty input check (age)
age = input("Enter your age: ").strip()

while age == "":
    print("You cannot enter an empty value!")
    age = input("Enter your age again: ").strip()

print(f"You are {age} years old")


print("-" * 20)


# 2. Password length validation
while True:
    password = input("Enter your password: ").strip()

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        continue  # go to next iteration

    print("Your password is valid")
    break


print("-" * 20)


# 3. Counter example
counter = 0

while counter < 5:
    print("Never give up!")
    counter += 1
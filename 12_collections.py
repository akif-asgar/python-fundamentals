# Collections are used to store multiple items in a single variable.

# There are four collection data types in the Python programming language:

# 1. List:
# Ordered, changeable, allows duplicates

# 2. Tuple:
# Ordered, unchangeable, allows duplicates

# 3. Set:
# Unordered, no duplicates

# 4. Dictionary:
# Key-value pairs, ordered, changeable, no duplicate keys


# ===================== Examples =====================

fruits = ["apple", "banana", "cherry"]  # list
cars = ("Ford", "BMW", "Volvo")  # tuple
sports = {"soccer", "basketball", "tennis"}  # set

# ===================== LIST OPERATIONS =====================

# Access
print(fruits[0])      # Gets first element
print(fruits[-1])     # Gets last element

# Add
fruits.append("orange")     # Adds item to the end
fruits.insert(1, "mango")   # Inserts item at specific index

# Remove
fruits.remove("banana")     # Removes specific value
fruits.pop()                # Removes last item
fruits.pop(0)               # Removes item at index
del fruits[0]               # Deletes item at index
# fruits.clear()            # Removes all items

# Update
fruits[0] = "kiwi"          # Changes value at index

# Info
print(len(fruits))          # Returns number of elements

# Loop
for item in fruits:
    print(item)             # Iterates through list

# Check
print("apple" in fruits)    # Checks if value exists (True/False)

# Sorting
fruits.sort()               # Sorts list ascending
fruits.sort(reverse=True)   # Sorts list descending

# Reverse
fruits.reverse()            # Reverses list order

# Copy
new_list = fruits.copy()    # Creates a copy of list

# Join
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)        # Combines two lists

# Count & Index
print(fruits.count("apple"))   # Counts occurrences of value
print(fruits.index("cherry"))  # Returns index of value


# ===================== TUPLE OPERATIONS =====================

# Access
print(cars[0])             # Gets first element
print(cars[-1])            # Gets last element

# Count & Index
print(cars.count("BMW"))   # Counts occurrences
print(cars.index("Volvo")) # Finds index

# Loop
for car in cars:
    print(car)             # Iterates through tuple

# Length
print(len(cars))           # Number of elements

# Convert (to modify)
temp = list(cars)          # Converts tuple to list
temp[0] = "Toyota"         # Modify value
cars = tuple(temp)         # Convert back to tuple

# Packing & Unpacking
(a, b, c) = cars           # Assigns values to variables
print(a, b, c)


# ===================== SET OPERATIONS =====================

# Add
sports.add("volleyball")          # Adds single item
sports.update(["golf", "swimming"]) # Adds multiple items

# Remove
sports.remove("tennis")     # Removes item (error if not found)
sports.discard("tennis")    # Removes item (no error)
sports.pop()                # Removes random item
# sports.clear()            # Removes all items

# Loop
for s in sports:
    print(s)                # Iterates through set

# Check
print("soccer" in sports)   # Checks existence

# Length
print(len(sports))          # Number of elements




# ===================== 2D COLLECTIONS =====================

# 2D collections are collections inside collections.
# Mostly used as rows and columns (like tables or matrices).

# ===================== 2D LIST =====================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
print(matrix[0])      # first row
print(matrix[0][1])   # element (row 0, col 1)

# Modify
matrix[1][1] = 50

# Add row
matrix.append([10, 11, 12])

# Remove row
matrix.pop()

# Loop
for row in matrix:
    for item in row:
        print(item)


# ===================== 2D TUPLE =====================

matrix_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access
print(matrix_tuple[1][2])

# Loop
for row in matrix_tuple:
    for item in row:
        print(item)


# ===================== 2D DICTIONARY =====================

students = {
    "s1": {"name": "John", "age": 20},
    "s2": {"name": "Alice", "age": 22}
}

# Access
print(students["s1"]["name"])

# Update
students["s1"]["age"] = 21

# Loop
for key, value in students.items():
    print(key, value)
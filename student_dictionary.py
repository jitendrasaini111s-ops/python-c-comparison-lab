# Representing the struct Student as a Python dictionary
student = {
    "roll": 101,
    "name": "Alice",
    "marks": 92.5
}

# Displaying the dictionary structure and types
for key, value in student.items():
    print(f"{key}: {value} (type: {type(value).__name__})")

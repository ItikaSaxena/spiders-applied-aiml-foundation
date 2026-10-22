
"""Exploring Python's built-in data structures."""

# List: stores multiple values and can be modified
subject_marks = [82, 76, 94, 82]
subject_marks.append(88)
print("Subject marks:", subject_marks)
print("Highest index example:", subject_marks[0])

# Tuple: stores values that cannot be modified
dimensions = (15, 25)
print("\nDimensions:", dimensions)

# Set: keeps only distinct values
distinct_marks = set(subject_marks)
print("Distinct marks:", distinct_marks)

# Dictionary: stores information as key-value pairs
student_details = {
    "name": "Itika Saxena",
    "course": "CSE AI/ML",
    "semester": 5
}

student_details["semester"] = 6

print("\nStudent details:", student_details)
print("Student name:", student_details["name"])

print("\nDisplaying each dictionary entry:")
for key, value in student_details.items():
    print(f"{key}: {value}")

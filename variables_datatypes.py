
# Demonstration of Python variables and data types

student_name = "Itika Saxena"
student_age = 20
student_height = 1.68
currently_studying = True

course_names = ["Python", "Machine Learning", "Data Structures"]
location = (30.3, 78.0)
programming_skills = {"Python", "C++", "Git"}
student_info = {
    "name": student_name,
    "age": student_age
}

print("Student Name:", student_name)
print("Age:", student_age)
print("Height in metres:", student_height)
print("Currently studying:", currently_studying)
print("Courses:", course_names)
print("Location coordinates:", location)
print("Skills:", programming_skills)
print("Student Information:", student_info)

print("\nData Type Details:")

values = {
    "student_name": student_name,
    "student_age": student_age,
    "student_height": student_height,
    "currently_studying": currently_studying,
    "course_names": course_names,
    "location": location,
    "programming_skills": programming_skills,
    "student_info": student_info
}

for variable, value in values.items():
    print(f"{variable} -> {type(value).__name__}")

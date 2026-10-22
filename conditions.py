
"""Calculate a student's grade using conditional statements."""

student_marks = float(input("Enter your marks (0-100): "))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks! Enter a value between 0 and 100.")

elif student_marks >= 90:
    print("Grade: A")
    print("Performance: Excellent")

elif student_marks >= 75:
    print("Grade: B")
    print("Performance: Very Good")

elif student_marks >= 60:
    print("Grade: C")
    print("Performance: Good")

elif student_marks >= 40:
    print("Grade: D")
    print("Performance: Needs Improvement")

else:
    print("Grade: F")
    print("Performance: Please work harder.")

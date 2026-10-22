
"""Demonstration of classes, objects, and methods."""


class Student:
    """Store student details and calculate average marks."""

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def calculate_average(self):
        """Calculate the average of the available marks."""
        if len(self.marks) == 0:
            return 0.0

        return sum(self.marks) / len(self.marks)

    def display_details(self):
        """Print student information."""
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")


if __name__ == "__main__":
    student_record = Student(
        "Itika Saxena",
        "CSE AI/ML",
        [82, 89, 94]
    )

    student_record.display_details()

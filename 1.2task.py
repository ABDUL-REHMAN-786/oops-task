# Task 1.2: Create a Student Class
# Your Own Practice:
# • Class: Student
# • Attributes: name, age, grade
# • Method: get_details() to print student info

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Creating an instance of the Student class
student1 = Student("John Doe", 16, "10th Grade")

# Calling the get_details method
student1.get_details()


# Explanation:
# The __init__ method initializes the attributes (name, age, and grade) when a new instance of the Student class is created.

# The get_details() method prints the student’s information in a readable format.

# If you run this code, it will create a student named "John Doe" who is 16 years old and in the 10th grade, then print those details using the get_details() method.


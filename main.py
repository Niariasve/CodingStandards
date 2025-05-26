"""Main"""

class Student:
    """Represents a student with grades and honors evaluation."""

    def __init__(self, student_id, name):
        """Student Class Constructor"""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, grade):
        """Add grades to student's grade list"""
        if isinstance(grade, (int, float)):
            self.grades.append(grade)

    def calc_average(self):
        """Calculates the average of student's grade list"""
        if not self.grades:
            return 0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        """Checks if student is elegible for honors """
        if self.calc_average() >= 90:
            self.honor = True

    def delete_grade(self, index):
        """Deletes a grade from student's grade list"""
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):
        """Presents students information"""
        print("ID: " + str(self.student_id))
        print("Name: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print(f"Average Grade: {self.calc_average():.2f}")
        print("Honor Roll: " + ("Yes" if self.honor else "No"))

def start_run():
    """Main function"""
    student = Student("x", "Alice")
    student.add_grades(100)
    student.add_grades(50)
    student.calc_average()
    student.check_honor()
    student.delete_grade(1)
    student.report()

start_run()

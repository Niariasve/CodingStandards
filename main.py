"""Main"""

class Student:
    """Represents a student with grades and honors evaluation."""

    def __init__(self, student_id, name):
        """Student Class Constructor"""
        if not student_id.strip() or not name.strip():
            raise ValueError("Student ID and Name cannot be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter_grade = "N/A"

    def add_grade(self, grade):
        """Add a valid grade to the student's record"""
        if not isinstance(grade, (int, float)):
            print(f"Invalid grade '{grade}': must be a number.")
            return
        if not 0 <= grade <= 100:
            print(f"Grade {grade} out of range (0–100).")
            return
        self.grades.append(grade)

    def calc_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Assign letter grade based on average"""
        avg = self.calc_average()
        if avg >= 90:
            self.letter_grade = 'A'
        elif avg >= 80:
            self.letter_grade = 'B'
        elif avg >= 70:
            self.letter_grade = 'C'
        elif avg >= 60:
            self.letter_grade = 'D'
        else:
            self.letter_grade = 'F'

    def determine_pass_fail(self):
        """Determine if the student passed"""
        self.is_passed = self.calc_average() >= 60

    def check_honor_roll(self):
        """Check if student qualifies for honor roll"""
        self.honor = self.calc_average() >= 90

    def delete_grade_by_index(self, index):
        """Remove grade by index, handle error gracefully"""
        try:
            removed = self.grades.pop(index)
            print(f"Removed grade at index {index}: {removed}")
        except IndexError:
            print(f"Index {index} is out of range.")

    def delete_grade_by_value(self, value):
        """Remove grade by value, handle missing value"""
        try:
            self.grades.remove(value)
            print(f"Removed grade: {value}")
        except ValueError:
            print(f"Grade {value} not found in record.")

    def generate_report(self):
        """Generate detailed student report"""
        self.determine_letter_grade()
        self.determine_pass_fail()
        self.check_honor_roll()

        print("----- Student Summary Report -----")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {self.calc_average():.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")
        print("----------------------------------")


def start_run():
    """Main test run"""
    try:
        student = Student("123", "Alice")
        student.add_grade(95.0)
        student.add_grade(85)
        student.add_grade(72.5)
        student.add_grade(-10)          # Invalid
        student.add_grade("A")          # Invalid

        student.delete_grade_by_index(1)
        student.delete_grade_by_index(10)  # Invalid index

        student.delete_grade_by_value(72.5)
        student.delete_grade_by_value(999)  # Invalid value

        student.generate_report()

    except ValueError as e:
        print("Error creating student:", e)


start_run()

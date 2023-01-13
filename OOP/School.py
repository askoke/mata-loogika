"""School class which stores information about courses and students."""
import random


class School:
    """Return a."""

    def __init__(self, name):
        """Return a."""
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        """Return a."""
        if course in self.courses:
            pass
        else:
            self.courses.append(course)

    def add_student(self, student):
        """Return a."""
        if student in self.students:
            pass
        else:
            id = random.randint(1, 100)
            while any(student.get_id() == id for student in self.students):
                id = random.randint(1, 100)
            student.set_id(id)
            self.students.append(student)

    def add_student_grade(self, student, course, grade: int):
        """Return a."""
        if student in self.students and course in self.courses:
            student.add_grade(tuple([course, grade]))
            course.add_grade(tuple([student, grade]))

    def get_students(self) -> list:
        """Return a."""
        return self.students

    def get_courses(self) -> list:
        """Return a."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list:
        """Return a."""
        for i in range(len(self.students) - 1):
            if self.students[i].get_average_grade() < self.students[i + 1].get_average_grade():
                help = self.students[i]
                self.students[i] = self.students[i + 1]
                self.students[i + 1] = help
        return self.students
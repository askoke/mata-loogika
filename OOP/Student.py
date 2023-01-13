"""Student class with student name and grades."""


class Student:
    """Return a."""

    def __init__(self, name: str):
        """Return a."""
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        """Return a."""
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        """Return a."""
        return self.id

    def get_grades(self) -> list:
        """Return a."""
        return self.grades

    def add_grade(self, grade):
        """Return a."""
        self.grades.append(grade)

    def get_average_grade(self):
        """Return a."""
        average_grade = 0
        if len(self.grades) == 0:
            return -1
        else:
            for grade in self.grades:
                average_grade += grade[1]
            average_grade = average_grade / len(self.grades)
            return average_grade

    def __repr__(self):
        """Return a."""
        return f"{self.name}"
"""Course class with name and grades."""


class Course:
    """Return a."""

    def __init__(self, name: str):
        """Return a."""
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Return a."""
        self.grades.append(grade)

    def get_grades(self) -> list:
        """Return a."""
        return self.grades

    def get_average_grade(self) -> float:
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
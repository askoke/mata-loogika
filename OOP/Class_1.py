"""Simple class."""


class Student:
    """Give a name for student."""

    def __init__(self, name, finished=False):
        """Retrun name and finished."""
        self.name = name
        self.finished = finished
"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        """Give student info."""
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """Return student id."""
        return self.__id

    def set_name(self, name):
        """Give name for the student."""
        self.__name = name

    def get_name(self):
        """Retrun student name."""
        return self.__name

    def set_status(self, status):
        """Give a status for the srudent."""
        if status == "Active" or status == "Expelled" or status == "Finished" or status == "Inactive":
            self.__status = status
        else:
            pass

    def get_status(self):
        """Return student status."""
        return self.__status
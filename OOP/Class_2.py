"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    firstname = ""
    lastname = ""
    age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    firstname = ""
    lastname = ""
    age = 0

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage

    # 3 x person usage

    # 3 x student usage
    pass

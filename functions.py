import math


def print_hello():
    print("Hello")
    pass

print_hello()


def get_hello():
    return "Hello"

print(get_hello())


def ask_name_and_greet_user():
    name = input("What's your name? : ")
    name = name.capitalize()
    print(f"Hi. {name} Would you like to have a Hamburger?")
    pass

ask_name_and_greet_user()


def calculate_hypotenuse_length(cathetus_a, cathetus_b):
    hypotenuse = math.sqrt((cathetus_a ** 2) + (cathetus_b ** 2))
    return hypotenuse

print(calculate_hypotenuse_length(3, 4))


def calculate_cathetus_length(cathetus_a, hypotenuse):
    cathetus_b = math.sqrt((hypotenuse ** 2) - (cathetus_a ** 2))
    return cathetus_b

print(calculate_cathetus_length(3, 5))
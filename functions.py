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
    if name == "Thanos"
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi. {name} Would you like to have a Hamburger?")
    pass

ask_name_and_greet_user()


def calculate_hypotenuse_length(cathetus_a, cathetus_b):
    if cathetus_a and cathetus_b is int:
        hypotenuse = math.sqrt((cathetus_a ** 2) + (cathetus_b ** 2))
    else:
        print("Use full numbers not numbers with decimals in the numbers!")
    return hypotenuse

print(calculate_hypotenuse_length(3, 4))


def calculate_cathetus_length(cathetus_a, hypotenuse):
    if cathetus_a and hypotenuse is int:
        cathetus_b = math.sqrt((hypotenuse ** 2) - (cathetus_a ** 2))
    else:
        print("Use full numbers not numbers with decimals in the numbers!")
    return cathetus_b

print(calculate_cathetus_length(3, 5))
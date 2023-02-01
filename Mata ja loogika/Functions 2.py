"""Function examples."""


def func():
    """Print string."""
    print("I´m inside the function")


def my_name_is(name):
    """Use inputed name for string."""
    print(f"My name is {name}")


def sum_six(num: int):
    """Add number six to a inputted number."""
    num = num + 6
    return num


def sum_numbers(a: int, b: int):
    """Give summery of a and b."""
    sum_ab = a + b
    return sum_ab


def usd_to_eur(euro: int):
    """Convert euros to dollars."""
    dollar = euro * 0.8
    return dollar
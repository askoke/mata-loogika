"""Loop exercises."""


def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    summery = 0
    if start < end:
        for number in range(start, end + 1):
            summery += number
        return summery
    elif start == end:
        return start


def sum_of_even_numbers(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    summery = 0
    if n > 0:
        for number in range(0, n + 1, 2):
            summery += number
        return summery
    elif n == 0:
        return 0


def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    summery = 0
    for number in range(n, end + 1, n):
        summery += number
    return summery


def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.

    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    summery = 0
    for number in numbers:
        summery += int(number)
    return summery


def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    multiplication = 1
    for number in range(start, end + 1):
        multiplication *= number
    return multiplication


def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    hola_string = ""
    for i in range(1, count + 1):
        hola_string = i * "hola"
    return hola_string


def compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.

    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    intress_rate = (1 + (rate / 100)) ** years
    compound_rate = amount * (intress_rate - 1)
    total_money = amount + compound_rate
    return total_money


def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.

    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    new_string = ""
    all_vowels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    for i in original_string:
        if i not in all_vowels:
             new_string += i
    return new_string
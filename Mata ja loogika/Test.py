"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if coffee_needed == False:
        if time >= 19 and time <= 24:
            return True
        elif time >= 1 and time <= 4:
            return True
        else:
            return False
    elif coffee_needed == True:
        if time >= 5 and time <= 18:
            return True
        else:
            return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    elif b == a and c == a:
        return 5
    elif b != a and c != a:
        return 1
    elif b == a or c == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    sum = 0
    if (big_baskets * 5) + small_baskets == ordered_amount:
        return small_baskets
    elif (big_baskets * 5) + small_baskets >= ordered_amount:
        sum = ordered_amount - (big_baskets * 5)
        return sum
    else:
        return -1

print(fruit_order(9, 5, 31))
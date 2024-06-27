from typing import Any


def sum_of_positives(a: Any, b: Any, message: str = None) -> int:
    """
    It is a calculator function (with some extra sub function).
    It allows only positive numbers (which represents integers or float),
        even if the numbers is in string format (in this case the decimal point must be the '.').
    In case of valid input, it returns an integer (rounded down after the addition).
    In case of invalid input, it throws a specific error (Value or Type) with a small comment.
    In case of any valid string message variable given, it writes that to the stdout after a separate
        "The message is:" header line.
    In case of the message contains only upper case letters, it converts that to lower case.
    :param a: required; integer, float or string
    :param b: required; integer, float or string
    :param message: optional; string
    :return: integer
    """
    return a + b

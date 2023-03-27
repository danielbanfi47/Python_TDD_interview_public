from typing import Any


def sum_of_positives(a: Any, b: Any, message: str = None) -> int:
    """
    It is a calculator function.
    It allows only positive numbers (integers or float),
    even if the numbers is in string format (in this case the decimal point must be the '.').
    In case of valid input it returns an integer (rounded down).
    In case of invalid input it throws a Value error with a small comment.
    In case of any valid string message variable given, it writes it to the stdout after a "The message is:" header line.
    In case of the message contains only upper case letters, it is converted to lower case
    :param a: required; integer, float or string
    :param b: required; integer, float or string
    :param message: optional; string
    :return: integer
    """
    return a + b

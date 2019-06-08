from typing import List, Tuple

CurrencyList = List[Tuple[str, str, float]]

# To the student:
# What is this `typing` stuff? Why are their colons in the argument list?
# This is an optional thing you can do in Python to specify the type of arguments
# or variables you are creating. It is not necessary, but it can help document
# what you expect. When I'm dealing with complex types like in this case, I like
# to use it to document what I'm doing. It does not change the behavior
# of the program.


def convert(rates: CurrencyList, value: float, current: str, target: str):
    """
    Converts a value from _current_ currency to _target_ currency.

    Arguments:

    - rates: a list of tuples showing the rate converting from, the rate converting to, and the exchange rate.
      For example: [("USD", "EUR", 0.74), ("USD", "JPY", 134.5)]
      This indicates that 1 US dollar is equal to 0.74 Euros and 1 US dollar is also equal to 134.5 Japanese yen.
    - value: the amount of currency you want to convert
    - current: the currency to convert from, like "USD"
    - target: the current to convert to, like "EUR"
    """
    pass

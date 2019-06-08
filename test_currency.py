from currency import convert
from pytest import approx

rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]


def test_converting_one_dollar_to_euros():
    assert convert(rates, 1, 'USD', 'EUR') == 0.74


# Uncomment when you are ready to run this test
# def test_converting_one_euro_to_dollars():
#     assert convert(rates, 1, 'EUR', 'USD') == approx(1.35)

# The rest of the tests are up to you to implement. Definitely
# test converting values that aren't 1, as well as the other tests
# specified in the README.md file.

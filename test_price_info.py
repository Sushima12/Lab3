import unittest
import price_info as PriceInfo

def test_total_cost_shopping():
    result = PriceInfo.total_cost_shopping()
    assert (result == 46.75) # Check if total cost is correct

def test_cost_of_fruits():
    fruit = 'papaya' # need to be a string
    quantity = 10000
    result = PriceInfo.cost_of_fruits(fruit, quantity)
    assert (result == 29500)


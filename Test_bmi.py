import unittest
import Lab_2.bmi as bmi

print("Test Lab_2")




def test_bmi_normal_weight():
    x = 1.78
    y = 63
    result = bmi.calculate_bmi(x,y)
    assert(result == 0)
def test_bmi_over_weight():
    x = 1.50
    y = 90
    result = bmi.calculate_bmi(x, y)
    assert (result == 1)
def test_bmi_under_weight():
    x = 1.78
    y = 40
    result = bmi.calculate_bmi(x, y)
    assert (result == -1)

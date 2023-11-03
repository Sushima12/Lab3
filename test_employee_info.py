import unittest
import employee_info as info

def test_get_employees_by_age_range():
    lower_limit = 20
    upper_limit = 30
    result = []
    result = info.get_employees_by_age_range(lower_limit, upper_limit)
    assert (result == [{'age': 25, 'department': 'Marketing', 'name': 'Jane', 'salary': 60000},
                        {'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}])

def test_calc_average_salary():
    result = info.calculate_average_salary()
    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    department = "Marketing"
    result = info.get_employees_by_dept(department)
    assert (result == [{'age': 25, 'department': 'Marketing', 'name': 'Jane', 'salary': 60000},
                        {'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}])
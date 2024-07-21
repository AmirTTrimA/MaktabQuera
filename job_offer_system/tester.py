"""
a tester module
"""
from main import User, FullNameError, AgeError, TimeConditionError, SalaryError

def test_user_class():
    """
    to test the user class
    """
    # Create a new user
    user = User()

    # Test default values
    assert user.id == 1  # First user should have ID 1
    assert user.name == ''  # Default name should be empty
    assert user.age == 0  # Default age should be 0
    assert user.time_condition == 'FULLTIME'  # Default time condition should be 'full'
    assert user.salary == 1000  # Default salary should be 1000

    # Test setting valid name
    user.name = "Alice"
    assert user.name == "Alice"

    # Test setting invalid name (should raise FullNameError)
    try:
        user.name = "A" * 11  # Exceeds maximum length
    except FullNameError:
        print(FullNameError())

    # Test setting valid age
    user.age = 25
    assert user.age == 25

    # Test setting invalid age (should raise AgeError)
    try:
        user.age = -1  # Invalid age
    except AgeError:
        print(AgeError())

    # Test setting valid time condition
    user.time_condition = 'PARTTIME'
    assert user.time_condition == 'PARTTIME'

    # Test setting invalid time condition (should raise TimeConditionError)
    try:
        user.time_condition = 'invalid_condition'  # Not a valid condition
    except TimeConditionError:
        print(TimeConditionError())

    # Test setting valid salary
    user.salary = 5000
    assert user.salary == 5000

    # Test setting invalid salary (should raise SalaryError)
    try:
        user.salary = -1000  # Invalid salary
    except SalaryError:
        print(SalaryError())

    # Test setting salary that is not a multiple of 1000 (should raise SalaryError)
    try:
        user.salary = 2500  # Not a valid salary
    except SalaryError:
        print(SalaryError())

    print("All tests passed!")

test_user_class()

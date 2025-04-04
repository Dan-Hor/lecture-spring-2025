from utils import is_valid_date


def test_is_valid_date_1():
    """
    Test function for is_valid_date().
    """
    # This one is missing a the extra varieble wich should make the test fail
    assert is_valid_date("2024-03-15") == True

    """
    assert is_valid_date("2024-02-29") == True  # Leap year
    assert is_valid_date("2024-02-30") == False  # Invalid day
    assert is_valid_date("2023-02-29") == False  # Not a leap year
    assert is_valid_date("2024/03/15") == False  # Wrong format
    assert is_valid_date("2024-13-01") == False  # Invalid month
    assert is_valid_date("2024-03-32") == False  # Invalid day
    """

#added a second test to test wrong output
def test_is_valid_date_2():
    # This is not valid since the input is type int and not a date
    assert is_valid_date("2024-03-15", None) == False  # Invalid input

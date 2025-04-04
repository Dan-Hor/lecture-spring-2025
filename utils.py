import datetime

# Added a extra variebel to make the unit test fail 
def is_valid_date(date_string, extra):
    """
    Checks if a date is valid in the format "yyyy-mm-dd".

    Args:
        date_string: The date string to check.

    Returns:
        True if the date is valid, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

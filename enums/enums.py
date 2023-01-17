"""All enums have to be listed here"""
from enums.interfaces import CustomEnum


class TimeTypes(CustomEnum):
    """Usually used inside request body to determine
     which type of computations/filtering to perform"""
    WEEK = 1
    MONTH = 2


class Weekdays(CustomEnum):
    """Maps weekday with numbers and vice-versa to make code more readable and maintainable.
        Helps to convert datetime weekday index into human-readable format.
    """
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

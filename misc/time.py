"""Contains classes and methods for working with times(usually using datetime library)"""
from datetime import datetime, timezone, timedelta

from enums.enums import Weekdays

from misc.types import DeltaDatesGeneration


class Time:
    """Contains useful methods for working with UTC +0 times"""

    @classmethod
    def get_time_now(cls) -> datetime.now:
        """:returns current UTC +0 time(datetime)"""
        return datetime.now(timezone.utc)

    @classmethod
    def get_date_now(cls) -> datetime.date:
        """:returns today's UTC +0 date"""
        time_now = cls.get_time_now()
        return time_now.date()

    @classmethod
    def get_weekday(cls, date: datetime.date) -> Weekdays:
        """Converts date into weekday enum"""
        weekday_index: int = date.weekday()
        return Weekdays(weekday_index)

    @classmethod
    def str_to_date(cls, date: str, date_format: str = '%Y-%m-%d') -> datetime.date:
        """ Convert string into datetime date
            :param date - date of type string that has to be converted
            :param date_format - format of date parameter
        """
        return datetime.strptime(date, date_format).date()

    @classmethod
    def generate_dates_with_specified_deltas(cls,
                                             config: DeltaDatesGeneration) -> list[datetime.date]:
        """Not implemented at the moment! Execution of this method won't lead you to anything!
        Will be some kind of generate_days extension that will help to generate not only days,
        but month and year(may generate all at the same time)
        """

    @classmethod
    def generate_days(cls, number_of_days: int, reverse=False) -> list[datetime.date]:
        """Generates dates that start from today's date in forward or backward time sequence"""
        operation = -1 if reverse else 1
        date_now = cls.get_date_now()
        return [date_now + timedelta(days=i) * operation for i in range(number_of_days)]

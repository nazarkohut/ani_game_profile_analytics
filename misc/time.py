from datetime import datetime, timezone

from enums.enums import Weekdays
from datetime import timedelta


class Time:
    """Contains useful methods for working with UTC +0 times"""

    @classmethod
    def get_time_now(cls) -> datetime.now:
        return datetime.now(timezone.utc)

    @classmethod
    def get_date_now(cls) -> datetime.date:
        time_now = cls.get_time_now()
        return time_now.date()

    @classmethod
    def get_weekday(cls, date: datetime.date) -> Weekdays:
        """Converts date into weekday enum"""
        weekday_index: int = date.weekday()
        return Weekdays(weekday_index)

    @classmethod
    def str_to_date(cls, date: str, date_format: str = '%Y-%m-%d') -> datetime.date:
        return datetime.strptime(date, date_format).date()

    @classmethod
    def generate_days_with_specified_deltas(cls, date: datetime.date, number_of_days: int, reverse: bool = False,
                                            delta_years: int = 0, delta_months: int = 0,
                                            delta_days: int = 0) -> list[datetime.date]:
        pass

    @classmethod
    def generate_days(cls, number_of_days: int, reverse=False) -> list[datetime.date]:
        """Generates dates that start from today's date in forward or backward time sequence"""
        operation = -1 if reverse else 1
        date_now = cls.get_date_now()
        return [date_now + timedelta(days=i) * operation for i in range(number_of_days)]

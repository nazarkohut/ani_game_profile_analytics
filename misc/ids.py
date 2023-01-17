"""Contains (classes and methods) and functions to work with ids"""
import datetime


class TimeBasedIds:
    """Contains methods that help to work with IDs that have
        datetime, date, timestamps, etc., inside of it"""

    @classmethod
    def get_id(cls, date: datetime.date | datetime.datetime | datetime.time, user_id: str) -> str:
        """
        ::returns id(usually primary key) that is 'date and user_id'
        """
        return f"{date} {user_id}"

    @classmethod
    def get_ids(cls, dates: list[datetime.date], user_id: str) -> list[str]:
        """Generates list of ids in format: 'date user_id'"""
        return [cls.get_id(date, user_id) for date in dates]

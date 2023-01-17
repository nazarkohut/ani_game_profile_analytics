import datetime


class TimeBasedIds:
    @classmethod
    def get_id(cls, date: datetime.date, user_id: str) -> str:
        return f"{date} {user_id}"

    @classmethod
    def get_ids(cls, dates: list[datetime.date], user_id: str) -> list[str]:
        """Generates list of ids in format: 'date user_id'"""
        return [cls.get_id(date, user_id) for date in dates]

"""Contains classes and methods to perform week analytics retrieval"""
from config import container
from misc.ids import TimeBasedIds

from misc.time import Time


class WeekAnalytics:
    """Contains methods to perform week analytics retrieval, filtering and transformations"""

    @classmethod
    def add_week_labels(cls, items: list[dict[str, any]]) -> None:
        """Adds weekday key and value into list of dictionaries
            :param items - list of dictionaries that must contain key `date`
            where value for this key must be a valid datetime date
            that was converted into string
            :return nothing as it changes dictionaries in-place
        """
        for item in items:
            date = Time.str_to_date(item["date"])
            item["week_label"] = str(Time.get_weekday(date))

    @classmethod
    def retrieve_week_analytics(cls, user_id: str) -> list[dict[str, any]]:
        """Gets analytics for seven previous days, including today's date"""
        number_of_days_in_week = 7
        week_dates = Time.generate_days(number_of_days=number_of_days_in_week, reverse=True)
        week_ids = TimeBasedIds.get_ids(week_dates, user_id)

        query = "SELECT a.id, a.user_id, a.number_of_games, a.rating, a.date FROM AniGame as a " \
                "WHERE ARRAY_CONTAINS(@ids, a.id, false)"

        items = list(container.query_items(
            query=query,
            parameters=[dict(name="@ids", value=week_ids)],
            enable_cross_partition_query=True
        ))
        cls.add_week_labels(items)
        return items

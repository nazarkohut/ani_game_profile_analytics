from config import container
from misc.functions import TimeBasedIds

from misc.time import Time


class WeekAnalytics:
    @classmethod
    def add_week_labels(cls, items: list[dict[str, any]]) -> None:
        for item in items:
            date = Time.str_to_date(item["date"])
            item["week_label"] = str(Time.get_weekday(date))

    @classmethod
    def retrieve_week_analytics(cls, user_id: str) -> list[dict[str, any]]:
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

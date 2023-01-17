import json

from azure.cosmos import ContainerProxy
from azure.cosmos.exceptions import CosmosResourceNotFoundError

from misc.functions import TimeBasedIds
from misc.time import Time
from config import container


class EveryDayAnalytics:
    @classmethod
    def find_item(cls, item_id, container: ContainerProxy = container):
        """Searches for item inside container based on item id"""
        try:
            return container.read_item(item=item_id, partition_key=item_id)
        except CosmosResourceNotFoundError:
            return None

    @classmethod
    def create_analytics_item(cls, user: dict[str, any]) -> dict[str, any]:
        """Creates default analytics item"""
        date = Time.get_date_now()
        user_id = user['user_id']
        user_rating = user['user_rating']
        games_played_today = 0
        data = {
            "id": TimeBasedIds.get_id(date, user_id),
            "user_id": user_id,
            "number_of_games": games_played_today,
            "rating": user_rating,
            "date": str(date),
        }
        return data

    @classmethod
    def write_new_item_or_update_existing(cls, items, container: ContainerProxy = container) -> None:
        for (item, user) in items:
            if item is None:
                # print(f"Created {user.id} {item}")
                analytic_item = cls.create_analytics_item(user)
                container.create_item(analytic_item)
            else:
                item['rating'] = user["user_rating"]
                item['number_of_games'] = item['number_of_games'] + 1
                # print(f"Updated {user.id}")
                container.upsert_item(body=item)

    @classmethod
    def print_every_day_profile_analytics(cls, container: ContainerProxy = container, max_item_count: int = 10) -> None:
        query = "SELECT * FROM AniGame"
        params = []

        items = container.query_items(
            query=query, parameters=params, enable_cross_partition_query=True, max_item_count=max_item_count
        )

        for item in items:
            print(json.dumps(item, indent=True))

"""Contains classes and methods for gathering data within the day and helps you to work with it"""
import json

from azure.cosmos import ContainerProxy
from azure.cosmos.exceptions import CosmosResourceNotFoundError

from misc.ids import TimeBasedIds
from misc.time import Time
from config import container


class EveryDayAnalytics:
    """Makes working with everyday analytics container as easy as possible"""

    @classmethod
    def find_item(cls, item_id: any,
                  container: ContainerProxy = container):
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
    def write_new_item_or_update_existing(cls, items: list[tuple],
                                          container: ContainerProxy = container) -> None:
        """Runs through the list of items and writes an item inside the database container
        if the item with specified id does not exist. Otherwise, updates the existing item"""
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
    def print_every_day_profile_analytics(cls, container: ContainerProxy = container,
                                          max_item_count: int = 10) -> None:
        """Prints every item(or a limited number of items) from a particular container"""
        query = "SELECT * FROM AniGame"
        params = []

        items = container.query_items(
            query=query,
            parameters=params,
            enable_cross_partition_query=True,
            max_item_count=max_item_count
        )

        for item in items:
            print(json.dumps(item, indent=True))

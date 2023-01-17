"""Run this file to create everyday profile analytics container"""
from azure.cosmos import PartitionKey

from config import client

created_database = client.create_database_if_not_exists(id="AniGame")

partition_key_path = PartitionKey(path="/id")

created_container = created_database.create_container_if_not_exists(
    id="ProfileAnalytics", partition_key=partition_key_path, offer_throughput=400
)

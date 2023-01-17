"""Run this file to create everyday profile analytics container"""
from azure.cosmos import PartitionKey

from config import client, DATABASE_NAME, CONTAINER_NAME

created_database = client.create_database_if_not_exists(id=DATABASE_NAME)

partition_key_path = PartitionKey(path="/id")

created_container = created_database.create_container_if_not_exists(
    id=CONTAINER_NAME, partition_key=partition_key_path, offer_throughput=400
)

import os

from azure.cosmos import CosmosClient

ENDPOINT = os.getenv("AZURE_ENDPOINT")
KEY = os.getenv("AZURE_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

client = CosmosClient(url=ENDPOINT, credential=KEY)

database = client.get_database_client(DATABASE_NAME)

container = database.get_container_client(CONTAINER_NAME)

import os
from pymongo import MongoClient
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.exception import USvisaException
import sys


class MongoDBClient:
    client = None

    def __init__(self):
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable {MONGODB_URL_KEY} is not set")

                MongoDBClient.client = MongoClient(mongo_db_url)

            self.client = MongoDBClient.client
            self.database = self.client[DATABASE_NAME]

        except Exception as e:
            raise USvisaException(e, sys)

    
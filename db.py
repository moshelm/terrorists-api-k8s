from pymongo import MongoClient
import os


MONGO_HOST = os.getenv("MONGO_HOST","127.0.0.1")
MONGO_PORT = int(os.getenv("MONGO_PORT","27017"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME","admin")  
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD","secretpass")
MONGO_DB = os.getenv("MONGO_DB","threat_db")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE","admin")

class MongoManager():
    def __init__(self):
        # for checking
        # url = "mongodb://127.0.0.1:27017" 
        uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource={MONGO_AUTH_SOURCE}"
        self.client = MongoClient(uri)
        self.database = self.client[MONGO_DB]
        self.collection = self.database['top_threats']

    def insert_all(self,data:list[dict]):
        
        for record in data:
            self.collection.insert_one(record)




import pymongo


class MongoClient:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = None
        self.collections = {}

    def create_database(self, db_name: str):
        self.db = self.client[db_name]

    def create_collections(self, coll_name: str):
        self.collections[coll_name] = self.db[coll_name]

    def insert_item(self, coll_name: str, data: dict):
        return self.collections[coll_name].insert_one(data)

    def insert_items(self, coll_name: str, data: list[dict]):
        return self.collections[coll_name].insert_many(data)

    def truncate_collection(self, coll_name: str):
        self.collections[coll_name].delete_many({})

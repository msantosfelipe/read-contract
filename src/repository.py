from pymongo import MongoClient

class MongoRespository:
    def __init__(self, url, database, collection):
        client = MongoClient(url)
        db = client[database]
        self.collection = db[collection]

    def insert_contract(self, contract_data):
        inserted = self.collection.insert_one(contract_data.to_dict())
        return inserted.inserted_id

    def get_contract(self, inserted_id):
        return self.collection.find_one({"_id": inserted_id})


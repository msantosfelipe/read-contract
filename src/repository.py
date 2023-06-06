from pymongo import MongoClient
from datetime import datetime

class MongoRespository:
    def __init__(self, url, database, collection):
        client = MongoClient(url)
        db = client[database]
        self.collection = db[collection]

    def insert_contract(self, contract_data):
        dict = contract_data.to_dict()
        dict["data"] = datetime.strptime(dict["data"], "%d/%m/%Y")
        inserted = self.collection.insert_one(dict)
        return inserted.inserted_id

    def get_contract(self, inserted_id):
        contract = self.collection.find_one({"_id": inserted_id})
        contract["data"] = contract["data"].strftime("%d/%m/%Y")
        return contract

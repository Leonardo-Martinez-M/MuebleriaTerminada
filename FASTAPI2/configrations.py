from pymongo.mongo_client import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client.mueblesMongo 

collection = db["usuarios"]

collectionMuebles= db["muebles"]

collectionMateriales= db ["materiales"]



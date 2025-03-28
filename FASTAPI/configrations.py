from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://leomarman6:pass123@cluster0.c4xe1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.muebles_m
collection = db["usuarios"]



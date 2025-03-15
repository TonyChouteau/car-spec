from pymongo import MongoClient

MONGO_CLIENT = MongoClient("localhost", 27017)
DB = MONGO_CLIENT["garagehub"]
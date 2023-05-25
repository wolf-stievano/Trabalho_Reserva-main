# api/db.py
from pymongo import MongoClient

def get_db_collections(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client['Teste']
    reservations_collection = db['Reservas']
    users_collection = db['users']
    return reservations_collection, users_collection
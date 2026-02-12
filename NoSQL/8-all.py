#!/usr/bin/env python3
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
db=client.mydatabase
collection=db.mycollection
listed=collection.find({})
return listed

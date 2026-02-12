#!/usr/bin/env python3
"""Insert document"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """Update topics """
    result = mongo_collection.update_one(
        {'name': name, '$or': [{'topics': {'$exists': False}}, {'topics': []}]}, 
        {'$set':{'topics':topics}}
    )

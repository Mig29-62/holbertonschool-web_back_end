#!/usr/bin/env python3
"""Insert document"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """we insert new document and return id"""
    result = mongo_collection.insert_one(kwargs)  # Insert the document
    return result.inserted_id 

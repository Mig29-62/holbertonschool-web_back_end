#!/usr/bin/env python3
"""Insert document"""

from pymongo import MongoClient

def update_topics(mongo_collection,name,topics):
    """we insert new document and return id"""
    result = mongo_collection.update(name,topics) 

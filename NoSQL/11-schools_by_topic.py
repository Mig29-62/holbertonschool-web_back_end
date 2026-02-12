#!/usr/bin/env python3
"""F.I.N.D"""

from pymongo import MongoClient

def schools_by_topic(mongo_collection,topic):
    """ we use find function"""
    result = mongo_collection.find(topic)  
    return result 

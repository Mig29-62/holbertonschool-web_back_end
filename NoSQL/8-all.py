#!/usr/bin/env python3
"""intro of the module"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """using find to list all documents"""
    listed = mongo_collection.find({})
    return listed

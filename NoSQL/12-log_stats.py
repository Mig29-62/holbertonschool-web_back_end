#!/usr/bin/env python3
"""
this module provides stats about Nginx logs stored in MongoDB.
it connects to the logs database and analyzes the nginx collection.
"""
from pymongo import MongoClient


def statistica():
    """
    we calculate the total number of logs and also print out other statistics
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    statistica()

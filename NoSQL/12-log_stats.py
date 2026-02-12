#!/usr/bin/env python3
"""Nginx log stats from MongoDB"""

from pymongo import MongoClient

def get_nginx_stats():
    """Fetches stats from the Nginx logs in MongoDB.
       Counts the total number of logs and breaks it down by HTTP method.
       Also counts the number of GET requests to the /status path."""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx
    """we count the total logs using count function and the same for every method"""
    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    """we print total logs and using loop print ip for every other method"""
    print(f"{total_logs} logs")
    for method in methods:
        print(f"\t{method}: {method_counts[method]} logs")
    print(f"GET /status: {get_status_count} logs")
if __name__ == "__main__":
    get_nginx_stats()
	

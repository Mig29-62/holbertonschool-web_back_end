#!/usr/bin/env python3
"""Nginx log stats from MongoDB"""

from pymongo import MongoClient

def get_nginx_stats():
    """Fetches stats from the Nginx logs in MongoDB."""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx
    
    total_logs = collection.count_documents({})
    
    if total_logs == 0:
        print("0 logs")
        print("Methods:")
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            print(f"\tmethod {method}: 0")
        print("GET /status: 0 logs")
        return

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"GET /status: {get_status_count} logs")

if __name__ == "__main__":
    get_nginx_stats()

#!/usr/bin/env python3
"""Nginx log stats from MongoDB"""

from pymongo import MongoClient

def get_nginx_stats():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx
    
    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{total_logs} logs")
    for method in methods:
        print(f"\t{method}: {method_counts[method]} logs")
    print(f"GET /status: {get_status_count} logs")

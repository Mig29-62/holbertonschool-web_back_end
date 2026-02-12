#!/usr/bin/env python3
"""
A script to log statistics from the NGINX logs collection in MongoDB.
It counts the total number of logs, the count of each HTTP method, and the count of '/status' checks.
"""
from pymongo import MongoClient

def log_stats():
    """
    Logs statistics from the NGINX collection in MongoDB, including:
    - Total number of logs
    - Counts for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - The number of '/status' checks.
    """
    
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs in the collection
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs\n")

    # Methods section
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"method {method}: {method_count}")
    
    # Count '/status' checks for the 'GET' method
    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\n{status_checks} status check")

if __name__ == "__main__":
    log_stats()

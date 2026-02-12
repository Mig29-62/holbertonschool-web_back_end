#!/usr/bin/env python3
"""
this module provides stats about Nginx logs stored in MongoDB.
it connects to the logs database and analyzes the nginx collection.
"""

from pymongo import MongoClient


def analyze_nginx_logs():
    """filling there as per rules (required to document more)"""

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
    analyze_nginx_logs()

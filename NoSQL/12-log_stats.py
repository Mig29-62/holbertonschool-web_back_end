#!/usr/bin/env python3
"""
statistical data provider
"""

from pymongo import MongoClient


def analyze_nginx_logs():
    """filling there because not enough documentation apparently:))"""
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    """we  basically just get numbers out of logs,match them and print them in beautiful styles"""
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

#!/usr/bin/env python3
"""Provides statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats() -> None:
    """Display Nginx logs statistics from logs.nginx collection."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
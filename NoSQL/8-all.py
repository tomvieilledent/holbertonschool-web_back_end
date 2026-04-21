#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list of all documents in a MongoDB collection.

    Args:
            mongo_collection: pymongo collection object.

    Returns:
            A list of documents. Returns an empty list when the collection
            has no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())

#!/usr/bin/env python3
"""
Python function that inserts a new doc in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new doc into a database."""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id

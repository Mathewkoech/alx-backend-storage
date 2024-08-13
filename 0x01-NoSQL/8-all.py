#!/usr/bin/env python3
""" a function that returns a list of all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    param mongo_collection: pymongo collection object
    return: list of documents in the collection, or
        an empty list if no document
    """
    return list(mongo_collection.find())

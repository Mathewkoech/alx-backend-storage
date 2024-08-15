#!/usr/bin/python3

import uuid
import redis
import functools
from typing import Union, Optional, Callable


def count_calls():
class Cache:
    """
    Handles data storage and retrieval in Redis using unique keys.

    Attributes:
        _redis (redis.Redis): An instance of the Redis client.
    """

    def __init__(self, host='localhost', port=6379, db=0):
        """
        Initializes Redis client and clears any existing data.
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis under a unique key and returns the key.

        Args:
            data: Data to store. can be srt, bytes, int or float.

        Returns:
            The unique key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Retrieves data from Redis by key and
        converts it using the provided function.

        Args:
            key: The key of the data to retrieve.
            fn: An optional callable to convert the data back to
            its desired format.

        Returns:
            The retrieved data, optionally converted using fn or None
            if key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn:
            callable_fn = fn(data)
            return callable_fn
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string from Redis.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The retrieved string or None if the key doesn't exist.
        """
        value = self._redis.get(key, fn=lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The retrieved integer or None if key doesn't exist.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            return None

        return value


    


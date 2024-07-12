#!/usr/bin/env python3

import asyncio
from typing import List
from 0x01-python_async_function.0-main import wait_random

"""
Module for concurrent coroutines
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for random delays and returns a list of the resulting delays.

    Args:
        n (int): The number of times to call the wait_random function.
        max_delay (int): The maximum delay value for each call to wait_random.

    Returns:
        List[float]: A list of the resulting delays.

    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

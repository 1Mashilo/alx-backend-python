#!/usr/bin/env python3
"""
This module contains a function to measure
the runtime of asynchronous coroutines.

Functions:
    measure_time: Measures the average runtime
    of a specified number of coroutines.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

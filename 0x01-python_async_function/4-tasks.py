#!/usr/bin/env python3
"""
This module contains a function to create
multiple asyncio tasks and gather their results.

Functions:
    task_wait_n: Creates multiple asyncio tasks and
    returns their results in sorted order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates multiple asyncio tasks and
    returns their results in sorted order.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of results from the tasks,
        sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

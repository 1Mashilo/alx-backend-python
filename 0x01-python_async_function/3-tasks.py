#!/usr/bin/env python3
"""
This module contains a function to create asyncio tasks.

Functions:
    task_wait_random: Creates an asyncio task for the wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))

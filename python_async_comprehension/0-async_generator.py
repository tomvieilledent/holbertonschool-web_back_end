#!/usr/bin/env python3
"""Module for asynchronous generator coroutines."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that yields random floats asynchronously.
    
    Loops 10 times, waiting 1 second each iteration before yielding
    a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


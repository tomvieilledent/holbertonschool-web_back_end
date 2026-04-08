#!/usr/bin/env python3
"""Module for creating async comprehensions from async generators."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect all values from async_generator into a list.
    
    Uses async comprehension to iterate through the async generator
    and accumulate all yielded float values into a single list.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result

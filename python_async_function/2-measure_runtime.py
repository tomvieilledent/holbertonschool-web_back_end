#!/usr/bin/env python3
"""Measure runtime of concurrent coroutines."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: float) -> float:
    """Measure average execution time for wait_n coroutines."""
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()

    return float((end - start)/n)

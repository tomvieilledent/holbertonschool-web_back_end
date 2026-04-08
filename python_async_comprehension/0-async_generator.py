#!/usr/bin/env python3
'''Async Generator on va ecrire ca pour que ca soit plus long'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generaton[float, None, None]: # type: ignore
    '''Yield 10 random floats. Cest trop court donc j'en rajoute'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

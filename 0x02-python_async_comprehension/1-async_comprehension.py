#!/usr/bin/env python3
"""Collects 10 random numbers using an
async comprehension over async_generator."""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an
    async comprehension over async_generator."""
    return [_ async for _ in async_generator()]

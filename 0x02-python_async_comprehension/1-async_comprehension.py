#!/usr/bin/env python3
"""Collects 10 random numbers using an
async comprehension over async_generator."""
from typing import List
import asyncio
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an
    async comprehension over async_generator."""
    return [number async for number in async_generator()]

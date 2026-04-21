#!/usr/bin/env python3
"""Pagination utility module."""


def index_range(page, page_size) -> tuple[int, int]:
    """Return start and end indices for a given page."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

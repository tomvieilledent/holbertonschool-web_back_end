#!/usr/bin/env python3
"""Pagination with simple page and page_size parameters."""
import csv
import math
from typing import List


def index_range(page, page_size) -> tuple[int, int]:
    """Return start and end indices for a given page."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page from the dataset."""
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return pagination data with hypermedia metadata."""
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"
        data = self.dataset()
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data[start:end],
            "next_page": page + 1 if end < len(data) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

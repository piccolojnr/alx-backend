#!/usr/bin/env python3
"""Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for the given pagination parameters.

    :param page: int - the current page number (1-indexed)
    :param page_size: int - the number of items per page
    :return: tuple - (start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        :param page: int - the current page number (1-indexed)
        :param page_size: int - the number of items per page
        :return: list - the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10,
    ) -> Dict[str, Optional[int]]:
        """
        Returns a dictionary with the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page
        - next_page: the next page number or None if no next page
        - prev_page: the previous page number or None if no previous page
        - total_pages: the total number of pages in the dataset as an int
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages,
        }

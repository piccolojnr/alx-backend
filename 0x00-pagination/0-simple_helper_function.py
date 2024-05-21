#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple


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

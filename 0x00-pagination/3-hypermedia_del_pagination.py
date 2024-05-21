#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            dd = {i: dataset[i] for i in range(len(dataset))}
            self.__indexed_dataset = dd

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing
        pagination information
        for deletion-resilient pagination.

        :param index: int - the current
        start index of the return
        page (default is None)
        :param page_size: int - the number
        of items per page (default is 10)
        :return: dict - a dictionary with
        pagination information
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        dataset_keys = sorted(dataset.keys())

        if index is None:
            index = 0

        current_index = index
        data = []
        count = 0

        while count < page_size and current_index < len(dataset_keys):
            key = dataset_keys[current_index]
            if key in dataset:
                data.append(dataset[key])
                count += 1
            current_index += 1

        if current_index < len(dataset_keys):
            next_index = current_index
        else:
            next_index = None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }

#!/usr/bin/env python3
""" simple pagination """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ returns start index and end index corresponding to
    range of indexes for the pagination parameters
    page numbers are 1-indexed"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        data = self.dataset()
        if page * page_size > len(data):
            return []
        start, stop = index_range(page=page, page_size=page_size)
        return data[start: stop]

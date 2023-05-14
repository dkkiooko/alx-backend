#!/usr/bin/env python3
""" hypermedia pagination """
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
        """ gets pages from the input pagination requirements """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        try:
            data = self.dataset()
            start, stop = index_range(page=page, page_size=page_size)
            return data[start: stop]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ returns dictionary with key value pairs """
        data = self.get_page(page=page, page_size=page_size)
        data_set = self.dataset()
        lenDataset = len(data_set) if data_set else 0

        total_pages = math.ceil(lenDataset / page_size) if data_set else 0
        page_size = len(data) if data else 0

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        hypermedia = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return hypermedia

#!/usr/bin/env python3
""" helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ returns start index and end index corresponding to
    range of indexes for the pagination parameters
    page numbers are 1-indexed"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

#!/usr/bin/env python3
"""
script with a function index_range that takes two
integer arguments page and page_size
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function return aa tuple of the start and end index
    of the requested page content
    """

    return ((page-1) * page_size, page * page_size)

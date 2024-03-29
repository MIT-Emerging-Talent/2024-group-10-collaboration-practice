import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from quick_sort import quick_sort


class TestQuickSortV1(unittest.TestCase):
    '''
    Test cases for the quick_sort function.

    These tests cover various scenarios including empty arrays,
    arrays with a single element, arrays in increasing order,
    arrays in decreasing order, and arrays in random order.
    '''
    def test_empty_array(self):
        array = list()
        result = list()

        self.assertEqual(quick_sort(array), result)

    def test_single_element(self):
        array = [1]
        result = [1]

        self.assertEqual(quick_sort(array), result)

    def test_increasing_order(self):
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(quick_sort(array), result)

    def test_decreasing_order(self):
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(quick_sort(array), result)

    def test_random_order(self):
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(quick_sort(array), result)

if __name__ == "__main__":
    unittest.main()

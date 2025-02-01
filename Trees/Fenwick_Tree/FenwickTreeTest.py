import unittest
from sys import *
path.append("../DATA STRUCTURE")
from Trees.Fenwick_Tree.Fenwick_Tree import FenwickTree


class TestFenwickTree(unittest.TestCase):
    def test_initialization_with_size(self):
        # Test initialization with size
        ft = FenwickTree(5)
        self.assertEqual(len(ft.tree_arr), 5)
        self.assertEqual(all(x == 0 for x in ft.tree_arr), True)

    def test_initialization_with_array(self):
        # Test initialization with array
        arr = [1, 2, 3, 4, 5]
        ft = FenwickTree(arr)
        self.assertEqual(len(ft.tree_arr), len(arr))

    def test_prefix_sum(self):
        # Test prefix sum calculations
        arr = [1, 2, 3, 4, 5] # [0, 1, 2, 3, 4, 5]
        ft = FenwickTree(arr)
        
        # Test various prefix sums
        self.assertEqual(ft.prefix_sum(0), 1)  # Sum up to index 0
        self.assertEqual(ft.prefix_sum(2), 6)  # Sum up to index 2 (1+2+3)
        self.assertEqual(ft.prefix_sum(4), 15)  # Sum up to index 4 (1+2+3+4+5)

    def test_range_sum(self):
        # Test range sum calculations
        arr = [1, 2, 3, 4, 5]
        ft = FenwickTree(arr)
        
        # Test various ranges
        self.assertEqual(ft.range_sum(0, 2), 6)  # Sum from index 0 to 2
        self.assertEqual(ft.range_sum(1, 3), 9)  # Sum from index 1 to 3
        self.assertEqual(ft.range_sum(2, 4), 12)  # Sum from index 2 to 4

    def test_update(self):
        # Test update operation
        arr = [1, 2, 3, 4, 5]
        ft = FenwickTree(arr)
        
        # Update value at index 2
        ft.update(2, 2)  # Add 2 to element at index 2
        self.assertEqual(ft.prefix_sum(2), 8)  # New sum should be 8 (1+2+5)

    def test_edge_cases(self):
        # Test empty tree
        ft = FenwickTree(0)
        self.assertEqual(len(ft.tree_arr), 0)

        # Test single element
        ft = FenwickTree([1])
        self.assertEqual(ft.prefix_sum(0), 1)

    def test_negative_numbers(self):
        # Test with negative numbers
        arr = [-1, -2, -3, -4, -5]
        ft = FenwickTree(arr)
        self.assertEqual(ft.prefix_sum(2), -6)  # Sum up to index 2
        self.assertEqual(ft.range_sum(1, 3), -9)  # Sum from index 1 to 3

    def test_large_numbers(self):
        # Test with large numbers
        arr = [1000000, 2000000, 3000000]
        ft = FenwickTree(arr)
        self.assertEqual(ft.prefix_sum(2), 6000000)

if __name__ == '__main__':
    unittest.main()
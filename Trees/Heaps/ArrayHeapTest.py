import unittest
from ArrayHeap import Min_Heap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        """Set up a new empty heap before each test"""
        self.heapArray = Min_Heap()

    def tearDown(self):
        """Clear the heap after each test"""
        self.heapArray = Min_Heap()

    def test_initialization(self):
        """Test heap initialization"""
        # Test empty initialization
        empty_heap = Min_Heap()
        self.assertEqual(empty_heap.size, 0)
        self.assertEqual(empty_heap.heap, [])

        # Test initialization with list
        init_heap = Min_Heap([5, 3, 7, 1, 4, 6])

        self.assertEqual(init_heap.size, 6)
        self.assertEqual(init_heap.peek(), 1)  # Should be heapified

    def test_peek(self):
        """Test peek operation"""
        # Test peek on empty heap
        heapArray = Min_Heap([])
        self.assertIsNone(heapArray.peek())

        # Test peek with elements
        heapArray = Min_Heap([3, 5, 7])

        self.assertEqual(heapArray.peek(), 3)


    def test_insert(self):
        """Test insert operation"""
        values = [5, 3, 7, 1, 4, 6]
        for val in values:
            self.heapArray.insert(val)
        
        self.assertEqual(self.heapArray.size, 6)
        self.assertEqual(self.heapArray.peek(), 1)  # Minimum should be at root
        

    def test_extract_min(self):
        """Test extract_min operation"""
        # Test extract_min on empty heap
        self.assertIsNone(self.heapArray.extract_min())

        # Test extract_min with elements
        self.heapArray = Min_Heap([5, 3, 7, 1, 4, 6])
        self.assertEqual(self.heapArray.extract_min(), 1)
        self.assertEqual(self.heapArray.extract_min(), 3)
        self.assertEqual(self.heapArray.size, 4)


    def test_change_key(self):
        """Test change_key operation"""
        self.heapArray = Min_Heap([5, 3, 7, 1, 4, 6])
        
        # Test decreasing a key
        self.heapArray.change_key(2, 0)  # Change 7 to 0
        self.assertEqual(self.heapArray.peek(), 0)  # Should bubble up to root
        
        # Test increasing a key
        self.heapArray.change_key(1, 10)  # Change a value to 10
        self.assertNotEqual(self.heapArray.peek(), 10)  # 10 should not be at root
        
        # Test invalid index
        with self.assertRaises(AssertionError):
            self.heapArray.change_key(10, 5)
        

    def test_delete_key(self):
        """Test delete_key operation"""
        self.heapArray = Min_Heap([5, 3, 7, 1, 4, 6])
        original_size = self.heapArray.size
        
        # Test deleting a key
        self.heapArray.delete_key(2)
        self.assertEqual(self.heapArray.size, original_size - 1)
        
        # Test invalid index
        with self.assertRaises(AssertionError):
            self.heapArray.delete_key(10)


    def test_str_representation(self):
        """Test string representation"""
        self.heapArray = Min_Heap([1, 2, 3])
        self.assertEqual(str(self.heapArray), "[1, 2, 3]")

    def test_edge_cases(self):
        """Test edge cases"""
        # Single element
        single_heap = Min_Heap([1])
        self.assertEqual(single_heap.extract_min(), 1)
        self.assertEqual(single_heap.size, 0)
        
        # Duplicate values
        dup_heap = Min_Heap([1, 1, 1])
        self.assertEqual(dup_heap.extract_min(), 1)
        self.assertEqual(dup_heap.extract_min(), 1)
        self.assertEqual(dup_heap.size, 1)

if __name__ == '__main__':
    unittest.main()
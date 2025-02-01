from math import*

class Min_Heap:
 
    def __init__(self, List:list = []):
        '''
        Heapifies the given arrays as the data of the heap object.
        Time Complexity: O(n)
        Size Complexity: O(n)
        '''
        self.heap = List
        self.size = len(self.heap)
        if self.heap: self.heapify()

    def __str__(self):
        return str(self.heap)
    
    def __parent(self, index: int) -> int:
        '''
        Returns the index of the parent node of the given index.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        return ceil(index/2) - 1 if index != 0 else None

    def __left_child(self, index: int) -> int:
        '''
        Returns the index of the left child node of the given index.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        left_idx = (index * 2) + 1
        return  left_idx if left_idx < len(self.heap) else None 

    def __right_child(self, index: int) -> int:
        '''
        Returns the index of the right child node of the given index.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        right_idx = (index * 2) + 2
        return right_idx if right_idx < len(self.heap) else None
    
    def __swap(self, i: int, j: int):
        '''
        Swaps the elements at the given indices in the heap.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __drown(self, index: int):
        '''
        changes the given element index downwards until it sits on a valid position in the heap
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        right = self.__right_child(index) 
        left = self.__left_child(index) 

        while (left != None and self.heap[index] > self.heap[left] ) or (right != None and self.heap[index] > self.heap[right]):

            # if left child is smaller than the current node, swap the values
            if left != None and self.heap[index] > self.heap[left]:
                self.__swap(index, left)
                index = left
            
            # if left child is smaller than the current node, swap the values
            if right != None and self.heap[index] > self.heap[right]:
                self.__swap(index, right)
                index = right

                
            # Update the index of the children
            right = self.__right_child(index)
            left = self.__left_child(index)
      
    def __swim(self, index:int):
        '''
        Changes the given element index upwards until it sits on a valid position in the heap
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        parent = self.__parent(index)

        while parent != None and self.heap[parent] > self.heap[index]:
            self.__swap(parent, index)
            index = parent
            parent = self.__parent(index)
        
    def heapify(self) -> None:
        '''
        Heapifies the given arrays as the data of a min heap.
        Use If you appended Values to the heap using append() 
        Time Complexity: O(n)
        Size Complexity: O(1)
        '''
        # Start from last non-leaf node and move upwards
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.__drown(i) 
        
    def peek(self) -> int:
        '''
        Returns the minimum element in the heap without removing it.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        if self.heap:
            return self.heap[0]
        
    def extract_min(self) -> int:
        '''
        Removes and returns the minimum element from the heap, if the heap is empty returns None.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        if not self.heap: return None


        # Get the minimum element
        minimum =  self.heap[0]
        last_element = self.heap.pop()

        # If the heap is not empty, replace the root with the last element and drown the root to its correct position
        if self.size > 1:
            self.heap[0] = last_element
            self.__drown(0)
            
        self.size -= 1
        return minimum

    def change_key(self, index: int, new_value: int):
        '''
        changes the value of the element at the given index in the heap.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        assert index < self.size, "Heap index is out of bounds"

        # Replace the element at the given index with the new value and heapify the node downwards
        self.heap[index] = new_value
        parent_idx = self.__parent(index)

        # If the parent is larger than the current node, then swim the node upwards
        invalid_child =  parent_idx != None and self.heap[parent_idx] > self.heap[index]

        if invalid_child:
            self.__swim(index)
        else:
            self.__drown(index)
        
    def delete_key(self, index: int):
        '''
        Removes the element at the given index from the heap.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        assert index < self.size, "Heap index is out of bounds"
        
        # If the heap has only one element, remove it and return it
        if self.size == 1: 
            self.size -= 1
            return self.heap.pop()

        # Replace the element at the given index with the last element in the heap and heapify the root downwards
        self.heap[index] = self.heap.pop()
        parent_idx = self.__parent(index)
        self.size -= 1

         # If the parent is larger than the current node, then swim the node upwards
        invalid_child =  parent_idx != None and self.heap[parent_idx] > self.heap[index]

        if invalid_child:
            self.__swim(index)
        else:
            self.__drown(index)
    
    def insert(self, value: int):
        '''
        Inserts the value in the heap
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        self.heap.append(value)
        self.size += 1

        # Traverse the new value upwards until we reach a valid position
        index = self.size - 1
        self.__swim(index)
        
    
    
    
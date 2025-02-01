class FenwickTree:

    def __init__(self, input):
        '''
        Initializes a Fenwick Tree , efficiently calculates range sum in a static array of integers.
        Time complexity of construction: O(nlogn)
        Space complexity of construction: O(n)
        ''' 
        if isinstance(input, int):
            self.size = input + 1 
            self.tree_arr = [0] * (self.size)
        else:
            self.size = len(input) + 1
            self.tree_arr = [0] * (self.size)

            for i in range(len(input)):
                self.update(i, input[i])

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.tree_arr)

    @staticmethod
    def __LSB(i):
        '''
        Returns the least significant bit in a number.
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        return i & -i
    
    def prefix_sum(self, index:int) -> int:
        '''
        Returns the sum of the elements in the tree from index 1 to the given index.
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        '''

        # make the index 1-based

        index += 1
        res = 0

        while index > 0:
            res += self.tree_arr[index]
            index -= FenwickTree.__LSB(index)
        return res
        

    def range_sum(self, lower_bound:int, upper_bound:int) -> int:
        '''
        Returns the sum of the indices from lower_bound to upper_bound.
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        '''
        return self.prefix_sum(upper_bound) - self.prefix_sum(lower_bound)
        

    def update(self, index: int, value: int) -> None:
        '''
        Updates a node in the fenwick tree.
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        '''
        index += 1

        while index < self.size:
            self.tree_arr[index] += value
            index += FenwickTree.__LSB(index)
              
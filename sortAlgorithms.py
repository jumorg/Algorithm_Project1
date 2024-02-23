"""
Implementation of Bubble Sort 

Classes and Methods: 
    -bubbleSort(): 
        - 
"""
from caseScenario import caseScenario

class sortAlgorithms(): 
    def __init__(self): 
        self.arr = 0
    
    """
    Bubble : Implementation of the bubble sort algorithm 
    
        Sorting algorithm adapted from Dr. Chenyi Hu Lecutre Notes 
    """
    def bubbleSort(self, arr): 
        n = len(arr)
        
        for x in range(n): 
            swapped = False
            
            for i in range(1, n - x): 
                if arr[i - 1] > arr[i]: 
                    # Swap
                    arr[i], arr[i - 1] = arr[i - 1], arr[i] 
                    swapped = True
            
            # If no two elements were swapped, then break 
            if not swapped: 
                break
            
        return arr
    
    
    def mergeSort(self, m):
        if len(m) <= 1:
            return m
        # Splitting input array
        middle = len(m) // 2
        left = m[:middle]
        right = m[middle:]
        
        # Recursively sorting both halves
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        # Merging the sorted halves
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        left_idx, right_idx = 0, 0
        
        # Merge the two arrays into result
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        
        # Append any remaining elements of left
        if left_idx < len(left):
            result.extend(left[left_idx:])
        
        # Append any remaining elements of right
        if right_idx < len(right):
            result.extend(right[right_idx:])
        
        return result
    
    
    def quickSort():
        pass
    
    def timSort(): 
        pass
"""
sortAlgorithms.py

This class implements sorting algorithms including: Bubble Sort, Merge Sort, Quick Sort, and Insertion Sort. This
The algorithms are adapted from educational resources and optimized for educational purposes

Classes and Methods: 
    -sortAlgorithms():
        - bubbleSort(array): A comparison-based algorithm where each pair of adjacent elements are
        compared and the elements are swapped if not in ordered 
            -Time complexity: 
                Best: O(n)
                Average: O(n^2)
                Worst: O(n^2)
            
            Sorting algorithm adapted from Dr. Chenyi Hu Lecutre Notes 
            
        - mergeSort(array): Divide and conquer algorithm that divides the input array into two halves and
        calls itself for the two halves, and merges the two sorted halves
            - Time complexity: 
                Best: O(n log n)
                Average: O(n log n)
                Worst: O(n log n)
            
            This implementation is based on the mergeSort algorithm example found on Medium.com
            --> Article published by Pacticus AI on Nov 26, 2018. Available at https://medium.com/@Practicus-AI/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889

        - quickSort(array, begin, end): A divide and conquer algorithm that follows a systematic method for placing the elements
        of an array in order
            - Time complexity: 
                Best: O(n log n)
                Average: O(n log n)
                Worst: O(n^2)
            
            This implementation is based on the QuickSort algorithm example found on Medium.com
            --> Article published by Pacticus AI on Nov 26, 2018. Available at https://medium.com/@Practicus-AI/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
    
        - insertionSort(array): Builds final sorted array one item at a time
        
            - Time complexity: 
                Best: O(n)
                Average: O(n^2)
                Worst: O(n^2)

"""
from caseScenario import caseScenario

class sortAlgorithms(): 
    def __init__(self): 
        self.arr = 0
    
    """
    Bubble : Implementation of the bubble sort algorithm 
        Sorting algorithm adapted from Dr. Chenyi Hu Lecutre Notes 
    """
    def bubbleSort(self, array): 
        arrayLength = len(array)
        
        for pass_num in range(arrayLength): 
            swapped = False
            
            for i in range(1, arrayLength - pass_num): 
                if array[i - 1] > array[i]: 
                    
                    # Swap
                    array[i], array[i - 1] = array[i - 1], array[i] 
                    swapped = True
            
            # Stops if no swaps occurred
            if not swapped: 
                break
            
        return array
    
    """
    mergeSort: Divide and conquer algorithm that divides input array into two halves, calls itself for the two halves,
        and then merges the two sorted halves 
            
    This implementation is based on the mergeSort algorithm example found on Medium.com
    --> Article published by Pacticus AI on Nov 26, 2018. Available at https://medium.com/@Practicus-AI/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
    """
    def mergeSort(self, array):
        if len(array) <= 1:
            return array
        
        # split list, sort both halves, and merge them
        middle = len(array) // 2
        left = self.mergeSort(array[:middle])
        right = self.mergeSort(array[middle:])
        
        # Merging the sorted halves
        return self.merge(left, right)
    
    """
    merge: Helper function for mergeSort to merge the two sorted list
    """
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
 
    """
    quickSort: Initates the quickSort algorithm
        An sorting alogirhtm, serving as a systematic method for placing the elements of an array in order, following the 
        divide and conquer strategy
            
    This implementation is based on the QuickSort algorithm example found on Medium.com
        --> Article published by Pacticus AI on Nov 26, 2018. Available at https://medium.com/@Practicus-AI/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
    """
    def quickSort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1
            
        # Begin the iterative QuickSort process
        return self.iterativeQuickSort(array)
    
    """
    quickSort_partition: Heloper function for quickSort to partition the array 
    """
    def quickSort_partition(self, array, begin, end): 
        
        pivot_idx = begin
        
        # Go through array from the element next to pivot to the end
        for i in range(begin+1, end+1): 
            # If current element is less than or qual to pivot, it gets moved to the left of the pivot
            if array[i] <= array[begin]: 
                pivot_idx += 1
                
                # Swap the current element with the element at pivot_idx
                array[i], array[pivot_idx] = array[pivot_idx], array[i] 
        
        # Sawp the pivot element with the element at the final pivot index
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        
        return pivot_idx
    
    """
    iterativeQuickSort: Iterative version of QuickSort using a stack to keep track of the subarrays needed to be sorted
        The reseaon it is iterative and not recurisve is because when testing the O(n^2) (worst) time complexity, we keep 
        hitting the recursion limit and decided this was better than raising the recursion limit
    """
    def iterativeQuickSort(self, array): 
        # Initializes a stack with a tuple containing the range of the array
        stack = [(0, len(array) - 1)] 
        
        while stack: 
            begin, end = stack.pop()
            if begin >= end: 
                continue
            
            # Partition the array and gets the pivot index
            pivot_idx = self.quickSort_partition(array, begin, end)
            
            # Add subarrays to left and right of the pivot to the stack to partition again
            stack.append((begin, pivot_idx - 1))
            stack.append((pivot_idx + 1, end)) 
         
    """
    insertionSort: Sorting algorithm that builds final sorted array one item at a time
    """       
    def insertionSort(self, array): 
        
        for i in range(1, len(array)): 
            
            key = array[i] 
            
            # Moves elements for array greater than key one position ahead of their current position
            j = i - 1
            while j >= 0 and key < array[j]: 
                array[j + 1] = array[j]
                j -= 1
                
            array[j + 1] = key
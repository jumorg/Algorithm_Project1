import random
import timeit

class caseScenario(): 
    def __init__(self): 
        self.sizes = [100, 1000, 10000]
        self.size_index = 0 
    
    """
    measure_sort_time: Measures the execution time of a sorting function. 
    
    :param sort_function: The sorting function to measure
    :param arry: The array to sort
    :param number: How many times the execute the sort for timing
    :return: The execution time in seconds
    """
    def measure_sort_time(self, sort_function, array, number=1): 
        # Use a lambda to pass 'array' to the sorting function
        sort_time = timeit.timeit(lambda: sort_function(array), number=number)
        return sort_time

    def getNextSize(self): 
        # Get next size for testing
        if self.size_index < len(self.size) - 1: 
            self.size_index += 1
        else: 
            # Reset to inital size
            self.size_index = 0
        
        return self.sizes[self.size_index]

    """
    ascendingOrder: Initiates an array in ascendingOrder
    """
    def ascendingOrder(self, arraySize): 
        # Gets current array size
        if arraySize is None: 
            size = self.sizes[self.size_index]
        else: 
            size = arraySize
        
        # Generate array of given size with ascending order numbers
        ascendingOrder = list(range(1, size + 1))
        
        return ascendingOrder
    
    """
    randomOrder: Initiates an array with random integers
    """
    def randomOrder(self, arraySize): 
        min_val = 1
        
        if arraySize is None: 
            size = self.sizes[self.size_index]
        else: 
            size = arraySize
        
        # Generate array of given size with random integer values
        randomArray = [random.randint(min_val, size ) for _ in range(size)]
        
        
        return randomArray
    
    """
    descendingOrder: Sets an array in decending order
    """
    def descendingOrder(self, arraySize): 
        
        if arraySize is None: 
            size = self.sizes[self.size_index]
        else: 
            size = arraySize
        
        # Generate array of given size with decending order numbers
        worstCaseArray = list(range(size, 0, -1))
        
        return worstCaseArray
    
    def alternatingOrder(self, arraySize): 
        
        if arraySize is None: 
            size = self.sizes[self.size_index]
        else: 
            size = arraySize
            
        # Generate a sorted list of numbers 
        sorted_numbers = list(range(1, size + 1))
        alternatingArray = []
        
        # Append elements from start and end of sorted list in turn
        for i in range(size // 2): 
            alternatingArray.append(sorted_numbers[i]) 
            alternatingArray.append(sorted_numbers[-(i + 1)])
            
        # If size is odd, add middle elment at the end
        if arraySize % 2 != 0: 
            alternatingArray.append(sorted_numbers[size // 2])
            
        return alternatingArray
    

    
        
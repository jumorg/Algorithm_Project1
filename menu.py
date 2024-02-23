"""
Frontend Interface for Sorting Project                          ## Rename after picking file name

Classes and Methods: 
-frontEnd(): A class that encapsulates the frontend IO functionality
    - __init__(): Initializes the frontend with necessary instances 
    - start(): Starts the frontend interface, allowing user to choose which algorithm
    
    
"""
from caseScenario import caseScenario
from sortAlgorithms import sortAlgorithms

class frontEnd: 
    """
    __init__: Initialize the frontend with instances of caseScenario and sortAlgorithm
    """
    def __init__(self): 
        self.case_scenario = caseScenario()
        self.sort_algorithms = sortAlgorithms()
    
    """
    start: Starts the frontend interface
    """
    def start(self): 
        while True: 
            print("Welcome to the test suite of selected sorting algorithms!")
            
            print("\nSelect the sorting algorithm you want to test.")
            print("----------------------------------------------")
            print("1. Bubble Sort")
            print("2. Merge Sort") 
            print("3. Quick Sort")
            print("4. Tim Sort") 
            print("5. Exit")
            
            user_choice = input("Select a sorting algorithm (1-5): ")
            user_choice = int(user_choice) 
            
            # Process user selection
            if 1 <= user_choice <= 4:
                self.selectSortAlgorithm(user_choice)
            elif user_choice == 5: 
                print("\nHave a great day!")
                break 
            else: 
                print("Please enter a number between 1 and 5.")

    """
    SelectSortAlgorithm: Maps the user's choice to the corresponding sorting algorithm and 
                        starts the testing process
    """
    def selectSortAlgorithm(self, user_choice): 
        # Dictionary mapping user choices to sorting algorithm functions and their name
        algorithm_mapping = {
            1: (self.sort_algorithms.bubbleSort, "Bubble"),
            2: (self.sort_algorithms.mergeSort, "Merge"),
            3: (self.sort_algorithms.quickSort, "Quick"),
            4: (self.sort_algorithms.timSort, "Tim") 
        }
        
        # Retrieve the selected sorting function and its name based on user choice
        selected_sort, algorithm_name = algorithm_mapping.get(user_choice, (None, "Unkown"))
        
        if selected_sort: 
            self.testSort(selected_sort, algorithm_name)
        else: 
            print("Invalid selection.")
        
    """
    SortMenu: Menu for selecting the case scenario for user selected sort algorithm
    """
    def testSort(self, selected_sort, sort_name): 
        while True: 
            print(f"\nCase Scenarios for {sort_name} Sort")
            print("------------------------------")
            print("1. Best Case") 
            print("2. Average Case") 
            print("3. Worst Case") 
            print(f"4. Exit {sort_name} sort test")
                
            user_choice = input("Select the case (1-4): ")
            user_choice = int(user_choice) 
            
            # Define scenarios as a list for access by index
            scenarios = ["best", "average", "worst"]
            
            # If choice corresponds to one of the scenarios
            if 1 <= user_choice <= 3: 
                scenario = scenarios[user_choice - 1]
                
                # Call method to test sort with selected scenario
                self.testSortWithScenaro(selected_sort, scenario)
            elif user_choice == 4: 
                print("Going back to menu\n") 
                break
            else:
                print("\nPlease enter a number between 1 - 4")
    
    """
    testSort: Test sorting alogrithm with selected sorting function and scenario
    """
    def testSortWithScenaro(self, sort_function ,scenario): 
        print(f"\nIn {scenario} case: ")

        # Mapping of scenario names to their handling methods
        scenario_methods = { 
            "best": self.handleBestScenarios,
            "average": self.handleAverageScenarios, 
            "worst": self.handleWorstScenarios                   
        }
        
        # Gets chosen scenario
        scenario_method = scenario_methods.get(scenario)
        
        # Handles existing scenarios by calling the selected methods
        if scenario_method: 
            scenario_method(sort_function)
        else: 
            print("Invalid scenario")
            return
        
        # Allows user to input custom array size
        customSize, proceed = self.testCustomSize()
        if proceed:
            scenario_method(sort_function, customSize)

        
    """handleBestScenarios: Handles all cases with best scenarios (already sorted arrays) """
    def handleBestScenarios(self, sort_function, customSize = None): 
        # Checks if customSize is valid, if not use predetermined size 
        sizes = [customSize] if customSize else self.case_scenario.sizes
        
        for size in sizes: 
            # Measure and print the sorting time
            array = self.case_scenario.ascendingOrder(size)
            sort_time = self.case_scenario.measure_sort_time(sort_function, array)
            print(f"For N = {size}, it takes {sort_time:.8f} seconds")
    
    """handleAverageScenarios: Handles all cases with average scenarios (random number array)"""
    def handleAverageScenarios(self, sort_function, customSize = None): 
        # Checks if customSize is valid, if not use predetermined size 
        sizes = [customSize] if customSize else self.case_scenario.sizes
        
        for size in sizes: 
            # Measure and print the sorting time
            array = self.case_scenario.randomOrder(size)

            sort_time = self.case_scenario.measure_sort_time(sort_function, array)
            print(f"For N = {size}, it takes {sort_time:.8f} seconds")
    
    """handleworstScenarios: Handles all cases with worst scenarios"""
    def handleWorstScenarios(self, sort_function, customSize = None): 
        worst_caseScenario = {
            "bubbleSort": self.case_scenario.descendingOrder,
            "mergeSort": self.case_scenario.alternatingOrder,
            "quickSort": None,
            "timSort": None, 
        }
        # Checks if customSize is valid, if not use predetermined size 
        sizes = [customSize] if customSize else self.case_scenario.sizes
        
        # Gets name of sort function and matches with corresponding worst-case scenarios
        scenario_generator_name = sort_function.__name__
        scenario_generator = worst_caseScenario.get(scenario_generator_name)

        if not scenario_generator:
            print(f"No worst-case scenario defined for {scenario_generator_name}.")
            return

        for size in sizes:
            # Generate the array using the selected scenario generator
            array = scenario_generator(size)

            # Measure and print the sorting time
            sort_time = self.case_scenario.measure_sort_time(sort_function, array)
            print(f"For N = {size}, it takes {sort_time:.8f} seconds")
        
    """
    testCustomeSize: Prompt user to input a custom size for testing
    """
    def testCustomSize(self): 
        while True: 
            user_choice = input("Do you want to input another size (Y/N)? ").strip().upper() 
            if user_choice == 'Y': 
                n_value = int(input("What is the N? "))
                
                # Update size of array for generation
                return n_value, True
            elif user_choice == 'N': 
                return None, False
            else: 
                print("Please enter either Y or N!")
    
if __name__ == "__main__":
    front_end = frontEnd()
    front_end.start()
        
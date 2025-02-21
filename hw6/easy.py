def sum_array(arr):
    """
    Calculates the sum of all elements in the given list.

    :param arr: List of integers.
    :return: Sum of all integers in the list.
    
    Time Complexity: O(n) - We iterate through the list once.
    """
    return sum(arr)  # Built-in sum function runs in O(n) time complexity.

# Example test cases
print(sum_array([1, 2, 3, 4, 5]))  
print(sum_array([-10, 20, -30, 40]))  
print(sum_array([]))  


"""
AI promt
Write a Python function that takes a list of integers and returns the sum of all elements. Function Requirements
- The function should be named sum_array(arr).
- It should take one parameter: a list of integers.
- It should return the total sum of all numbers in the list.
- If the list is empty, return 0.
- The list may contain positive and negative number- The function should run in **O(n)** time complexity.
- Include a comment explaining this in the code.
"""
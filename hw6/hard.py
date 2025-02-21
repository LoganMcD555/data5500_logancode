def max_difference(arr):
    """
    Finds the maximum difference between any two numbers in the list.

    :param arr: List of integers.
    :return: The maximum difference between any two numbers, or None if not applicable.

    Time Complexity: O(n) - We traverse the list once to find min and max.
    """
    if len(arr) < 2:
        return None  # Not enough numbers to find a difference

    min_val = float('inf')
    max_val = float('-inf')

    for num in arr:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    return max_val - min_val

# Example test cases
print(max_difference([1, 2, 90, 10, 110])) 
print(max_difference([7, 1, 5, 3, 6, 4]))  
print(max_difference([10]))  


"""
AI promt

Write a Python function to find the **maximum difference** between any two numbers in a list of integers.
Function Requirnments
- Function name: max_difference(arr)
- Input: A list of integers
- Output: The maximum difference between any two numbers
- If the list has **less than two numbers**, return None
- Handle **positive and negative numbers**
- Optimize for efficiency
- The function should run in **O(n) time complexity**
- Include a comment explaining this

"""
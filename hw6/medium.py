def second_largest(arr):
    """
    Finds the second largest unique number in the given list.

    :param arr: List of integers.
    :return: The second largest unique integer, or None if not applicable.
    
    Time Complexity: O(n) - We iterate through the list once.
    """
    if len(arr) < 2:
        return None  # Not enough numbers to find second largest.

    first = second = float('-inf')  # Initialize first and second largest

    for num in arr:
        if num > first:  # New largest number found
            second, first = first, num
        elif first > num > second:  # New second largest found
            second = num

    return second if second != float('-inf') else None  # Return None if no second largest

# Example test cases
print(second_largest([10, 20, 4, 45, 99]))  
print(second_largest([5, 5, 5, 5]))  
print(second_largest([-10, -5, -2, -1]))  
print(second_largest([100])) 



"""
AI promt

- Write a Python function that finds the **second largest number** in a given list of integers.

Function Requirements
- The function should be named second_largest(arr).
- It should take a list of integers as input.
- It should return the second largest number in the list.
- If there is no second largest (e.g., list has 1 unique number or is empty), return None.
- The function should run in **O(n) time complexity**
- Include a comment explaining this

- If the list has less than two unique numbers, return None.
- The list may contain duplicate values.
- The list may have positive and negative numbers.


"""
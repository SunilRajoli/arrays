#Find Maximum and Minimum Element in an Array:

def find_max_min(arr):
    # Check if the array is empty
    if not arr:
        return None, None
    
    # Initialize max and min with the first element of the array
    max_elem = arr[0]
    min_elem = arr[0]
    
    # Iterate through the array to find maximum and minimum elements
    for num in arr:
        if num > max_elem:
            max_elem = num
        elif num < min_elem:
            min_elem = num
    
    return max_elem, min_elem

# Example usage:
arr = [3, 7, 2, 9, 1, 5]
max_elem, min_elem = find_max_min(arr)
print("Maximum element:", max_elem)
print("Minimum element:", min_elem)


"""
def find_max_min(arr):
    # Check if the array is empty
    if not arr:
        return None, None
    
    # Find the maximum and minimum elements using max() and min() functions
    max_elem = max(arr)
    min_elem = min(arr)
    
    return max_elem, min_elem

# Example usage:
arr = [3, 7, 2, 9, 1, 5]
max_elem, min_elem = find_max_min(arr)
print("Maximum element:", max_elem)
print("Minimum element:", min_elem)
"""
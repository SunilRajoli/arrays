#Find Missing Number

def find_missing_number(arr):
    # Calculate the expected sum of numbers from 0 to n
    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    
    # Calculate the sum of the given array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage:
arr = [3, 0, 1, 4, 5]
missing_number = find_missing_number(arr)
print("Missing number:", missing_number)

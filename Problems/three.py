#Remove Duplicates from Sorted Array

def remove_duplicates(arr):
    

    # Initialize index for the next unique element
    unique_index = 0

    # Iterate through the array
    for i in range(1, len(arr)):
        # If the current element is different from the last unique element
        if arr[i] != arr[unique_index]:
            # Move to the next unique element and update the array
            unique_index += 1
            arr[unique_index] = arr[i]

    # Resize the array to remove the duplicates
    del arr[unique_index + 1:]

    return arr

# Example usage:
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5]
result = remove_duplicates(arr)
print("Original array:", arr)
print("Array after removing duplicates:", result)

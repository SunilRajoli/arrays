#Rotate Array

def rotate_array(arr, k):
    # Calculate the effective rotation steps (k modulo the length of the array)
    k %= len(arr)
    
    # Split the array into two parts and concatenate them in the rotated order
    rotated_arr = arr[-k:] + arr[:-k]
    
    return rotated_arr

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print("Original array:", arr)
print(f"Array after rotating by {k} steps:", rotated_arr)
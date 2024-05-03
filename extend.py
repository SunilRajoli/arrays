import array

arr = array.array('i', [1, 2, 3, 4, 5])

print("The array before extend: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print()

arr.extend([6, 7, 8, 9, 10])
print("The array after extend: ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])

li = arr.tolist()

print("The new created list is: ", end=" ")
for i in range(0, len(li)):
    print(arr[i], end=" ")
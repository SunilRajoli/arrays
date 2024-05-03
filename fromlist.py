import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])

li = [1, 2, 4]

arr.fromlist(li)

print("The modified array is: ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
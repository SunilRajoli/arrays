import array as arr;
b = arr.array('i', [1, 2, 3])
print('Array before Append: ', end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4)
print('Array afetr Append: ', end=" ")
for i in (b):
    print(i, end=" ")
print()
# BubbleSort.py
array = [6, 8, 10, 4, 3, 5]
print(array)
i = 0
while i <= len(array)-2:
    j = 0
    while j <= len(array)-2-i:
        if array[j+1] < array[j]:
            swap = array[j]
            array[j] = array[j+1]
            array[j+1] = swap
        j += 1
    i += 1
print(array)

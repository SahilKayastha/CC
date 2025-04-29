def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
           
            if array[j] < array[min_index]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]

input_str = input("Enter numbers separated by spaces: ")
arr = [int(num) for num in input_str.split()]
size = len(arr)


selectionSort(arr, size)


print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

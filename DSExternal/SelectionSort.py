def SelectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]: #arr[j] > arr[min_index] for desc order
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[37,18,92,28,13,47,-298]
SelectionSort(arr)
print("The Sorted array is:", arr)

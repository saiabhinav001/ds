def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed at the correct position
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key element at its correct position
        arr[j + 1] = key

    return arr

arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
sorted_array = insertion_sort(arr)
print("Sorted array:", sorted_array)
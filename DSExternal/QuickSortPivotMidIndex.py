def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]
    left = low
    right = high - 1

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[high], arr[left] = arr[left], arr[high]
    return left

arr = [8, 6, 4, 7, 6, 8, 10, 12, 86, 54]
quicksort(arr, 0, len(arr) - 1)
print(arr)

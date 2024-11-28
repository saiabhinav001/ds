import random

def quicksort(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
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

arr = [10,7,8,9,1,5]
quicksort(arr, 0, len(arr) - 1)
print(arr)


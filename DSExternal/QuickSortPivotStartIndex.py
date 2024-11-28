def quicksort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]
    return right

arr = [8,6,4,7,6,8,10,12,86,54]
quicksort(arr,0,len(arr)-1)
print(arr)

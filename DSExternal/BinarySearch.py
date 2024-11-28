def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def binary_search(arr, target):
    # Perform binary search on a sorted array
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


def sort_and_search(arr, target):
    # Sort the array using Merge Sort
    merge_sort(arr)

    # Perform binary search on the sorted array
    return binary_search(arr, target)


arr = [30, 73, 25, 56, 5, 62]
target = 25

result_index = sort_and_search(arr, target)

if result_index != -1:
    print(f"Element {target} found at index {result_index} in the sorted array.")
else:
    print(f"Element {target} not found in the array.")

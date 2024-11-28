def linear_search(arr, x):
  n = len(arr)

  # Search through the array
  for i in range(0, n):
    if arr[i] == x:
      return i

  # Element not present
  return -1

arr = [2, 3, 4, 8, 20]
x = 4

# Function call
result = linear_search(arr, x)

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")
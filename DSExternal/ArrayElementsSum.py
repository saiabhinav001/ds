def sum_of_array_elements(arr):
    # Calculate the sum using the built-in sum() function
    return sum(arr)


# Main program
if __name__ == "__main__":
    # Input: User provides the array
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Calculate the sum
    result = sum_of_array_elements(array)

    # Output: Display the sum
    print("The sum of the elements in the array is:", result)

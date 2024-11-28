# Iterative method
def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Main program
if __name__ == "__main__":
    num = int(input("Enter a number to find its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Using the iterative method
        print("Factorial using iterative method:", factorial_iterative(num))

        # Using the recursive method
        print("Factorial using recursive method:", factorial_recursive(num))

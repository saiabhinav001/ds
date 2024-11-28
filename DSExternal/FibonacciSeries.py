# Normal iterative method
def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Wrapper to generate a Fibonacci series using the recursive method
def generate_fibonacci_recursive_series(n):
    return [fibonacci_recursive(i) for i in range(n)]


# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of terms for the Fibonacci series: "))

    # Using the iterative method
    print("Fibonacci series using iterative method:")
    print(fibonacci_iterative(n))

    # Using the recursive method
    print("Fibonacci series using recursive method:")
    print(generate_fibonacci_recursive_series(n))

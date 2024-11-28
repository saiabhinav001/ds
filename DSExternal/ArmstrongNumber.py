def is_armstrong_number(num):
    """Checks if a number is an Armstrong number.

    Args:
        num: The number to check.

    Returns:
        True if the number is an Armstrong number, False otherwise.
    """

    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    return num == sum

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
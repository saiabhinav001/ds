# Function to reverse a string using a stack
def reverse_string(input_string):
    stack = []  # Stack to hold characters

    # Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)

    # Pop all characters from the stack to reverse the string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Function to check if the input string is a palindrome
def is_palindrome(input_string):
    # Reverse the input string
    reversed_string = reverse_string(input_string)

    # Compare the original string with the reversed string
    return input_string == reversed_string

# Test the functions
input_string = "malayalam"

reversed_str = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_str}")

if is_palindrome(input_string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")

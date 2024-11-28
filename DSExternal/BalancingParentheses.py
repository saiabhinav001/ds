def is_balanced_parentheses(expression):
    """
    Check if the parentheses in the expression are balanced.

    :param expression: String containing parentheses
    :return: True if balanced, False otherwise
    """
    stack = []

    # Dictionary to match opening and closing parentheses
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # Stack should not be empty, and the top of the stack must match
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            stack.pop()  # Pop the matching opening bracket

    # If the stack is empty, parentheses are balanced
    return len(stack) == 0


# Test the function
if __name__ == "__main__":
    expressions = [
        "([])",  # Balanced
        "([{}])",  # Balanced
        "(]",  # Not Balanced
        "((())",  # Not Balanced
        "[(])",  # Not Balanced
        "{[()()]}",  # Balanced
    ]

    for expr in expressions:
        print(f"Expression: {expr} -> Balanced: {is_balanced_parentheses(expr)}")

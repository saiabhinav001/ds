def precedence(op):
    """Return the precedence of the operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    """Check if the character is an operator."""
    return c in '+-*/^'

def infix_to_postfix(expression):
    """
    Convert an infix expression to a postfix expression.

    :param expression: Infix expression as a string
    :return: Postfix expression as a string
    """
    stack = []  # Stack to hold operators
    result = []  # List to hold the postfix expression

    for char in expression:
        # If the character is an operand, add it to the result
        if char.isalnum():
            result.append(char)
        # If the character is '(', push it onto the stack
        elif char == '(':
            stack.append(char)
        # If the character is ')', pop and output from the stack until '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop the '('
        # If the character is an operator
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)

    # Pop all the operators left in the stack
    while stack:
        result.append(stack.pop())

    return ''.join(result)

infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix Expression:", infix_expr)
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)

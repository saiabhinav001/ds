def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.

    :param expression: Postfix expression as a string
    :return: Result of the evaluation
    """
    stack = []

    for char in expression:
        # If the character is an operand, push it onto the stack
        if char.isdigit():
            stack.append(int(char))
        # If the character is an operator, pop two operands from the stack
        elif char in '+-*/^':
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    # The result will be the only element left in the stack
    return stack[0]

postfix_expr = "53+82-*"
print("Postfix Expression:", postfix_expr)
result = evaluate_postfix(postfix_expr)
print("Evaluation Result:", result)

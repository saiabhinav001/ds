class Stack(object):
    def __init__(self, limit=2):
        self.stack = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if len(self.stack) >= self.limit:
            self.resize()  # Resize the stack dynamically
        self.stack.append(item)
        print("Stack after push:", self.stack)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]

    def resize(self):
        self.limit *= 2
        print("Stack resized, new limit:", self.limit)

# Create a stack with a limit of 2
stack = Stack(limit=2)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Pop an element from the stack
element = stack.pop()
print("\nPopped element:", element)

# Peek at the top element of the stack
top_element = stack.peek()
print("Top element:", top_element)

stack.push(60)
stack.push(70)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item onto the stack: {item}")
        self.display_stack()

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        popped_item = self.stack.pop()
        print(f"Popped item from the stack: {popped_item}")
        self.display_stack()
        return popped_item

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display_stack(self):
        print("Current stack:", self.stack)

# Function to handle user input
def stack_operations():
    my_stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Size of stack")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            item = input("Enter the item to push: ")
            my_stack.push(item)
        elif choice == "2":
            my_stack.pop()
        elif choice == "3":
            print("Top element:", my_stack.peek())
        elif choice == "4":
            if my_stack.is_empty():
                print("The stack is empty")
            else:
                print("The stack is not empty")
        elif choice == "5":
            print("Stack size:", my_stack.size())
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the function to start the program
stack_operations()
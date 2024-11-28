class Deque:
    def __init__(self):
        self.deque = []  # Initialize an empty list to represent the deque

    # Add to front operation: Insert an element at the front of the deque
    def add_front(self, item):
        self.deque.insert(0, item)
        print(f"Added to front: {item}")

    # Add to rear operation: Insert an element at the rear of the deque
    def add_rear(self, item):
        self.deque.append(item)
        print(f"Added to rear: {item}")

    # Remove from front operation: Remove and return the front element of the deque
    def remove_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque.pop(0)

    # Remove from rear operation: Remove and return the rear element of the deque
    def remove_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque.pop()

    # Peek front operation: Get the front element of the deque
    def peek_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque[0]

    # Peek rear operation: Get the rear element of the deque
    def peek_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque[-1]

    # Is Empty operation: Check if the deque is empty
    def is_empty(self):
        return len(self.deque) == 0

    # Size operation: Get the current size of the deque
    def size(self):
        return len(self.deque)

# Test the Deque implementation
deque = Deque()

deque.add_rear(10)
deque.add_rear(20)
deque.add_front(5)

print(f"Deque after additions: {deque.deque}")

print(f"Removed from front: {deque.remove_front()}")
print(f"Removed from rear: {deque.remove_rear()}")

deque.add_front(15)
deque.add_rear(25)

print(f"Front element: {deque.peek_front()}")
print(f"Rear element: {deque.peek_rear()}")
print(f"Deque size: {deque.size()}")
print(f"Deque is empty: {deque.is_empty()}")

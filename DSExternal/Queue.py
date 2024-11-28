class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    # Enqueue operation: Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
        self.display_queue()
    # Dequeue operation: Remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    # Front operation: Get the front element of the queue
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    # Is Empty operation: Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size operation: Get the current size of the queue
    def size(self):
        return len(self.queue)

    def display_queue(self):
        print("Current queue elements: ", self.queue)

# Test the Queue implementation
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"Dequeued: {queue.dequeue()}")
print(f"Front Element: {queue.front()}")
print(f"Queue Size: {queue.size()}")

queue.enqueue(40)
print(f"Dequeued: {queue.dequeue()}")
print(f"Queue Size: {queue.size()}")

# Priority Queue using Queue Data Structure

import queue
q=queue.PriorityQueue()
q.put(2)
q.put(4)
q.put(1)
q.put(0)
q.put(2)
q.put(6)
q.put(9)
for i in range(q.qsize()):
    print(q.get(i), end=" ")


'''import queue

def priority_queue_example():
    """
    Demonstrate the usage of PriorityQueue.
    """
    # Create a PriorityQueue instance
    pq = queue.PriorityQueue()

    # Add elements to the priority queue with their priority
    pq.put((3, "Task 3"))  # Priority 3
    pq.put((1, "Task 1"))  # Priority 1
    pq.put((2, "Task 2"))  # Priority 2
    pq.put((0, "Task 0"))  # Priority 0 (highest priority)

    print("Tasks in priority order:")
    while not pq.empty():
        # Get the task with the highest priority (lowest number)
        priority, task = pq.get()
        print(f"Priority: {priority}, Task: {task}")

# Test the priority queue
if __name__ == "__main__":
    priority_queue_example()'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printCLL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while True:
                print(n.data, "-->", end=" ")
                n = n.next
                if n == self.head:
                    break
            print()

    def add_begin(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            new_node.next = self.head
            n.next = new_node
            self.head = new_node

    def add_end(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head

    def add_before(self, item, x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == x:
            self.add_begin(item)
            return
        n = self.head
        while n.next != self.head:
            if n.next.data == x:
                break
            n = n.next
        if n.next == self.head:
            print("Node not found")
        else:
            new_node = Node(item)
            new_node.next = n.next
            n.next = new_node

    def add_after(self, item, x):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while True:
            if n.data == x:
                break
            n = n.next
            if n == self.head:
                print("Node not found")
                return
        new_node = Node(item)
        new_node.next = n.next
        n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                n = self.head
                while n.next != self.head:
                    n = n.next
                n.next = self.head.next
                self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                n = self.head
                while n.next.next != self.head:
                    n = n.next
                n.next = self.head

    def delete_value(self, x):
        if self.head is None:
            print("List is empty")
        elif self.head.data == x:
            self.delete_begin()
        else:
            n = self.head
            while n.next != self.head:
                if n.next.data == x:
                    break
                n = n.next
            if n.next == self.head:
                print("Node not found")
            else:
                n.next = n.next.next

CLL = CircularLinkedList()
CLL.add_begin(10)
CLL.add_begin(20)
CLL.add_end(30)
CLL.add_end(40)
CLL.add_before(25, 30)
CLL.add_after(35, 30)
CLL.printCLL()

CLL.delete_begin()
CLL.printCLL()

CLL.delete_end()
CLL.printCLL()

CLL.delete_value(25)
CLL.printCLL()

from node_jas import Node
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = last_node
            last_node.next = new_node
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                return
        if current.next == current:  # Solo hay un nodo en la lista
            self.head = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next

    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()



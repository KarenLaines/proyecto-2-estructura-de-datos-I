from node import Node
from typing import TypeVar, Generic

T = TypeVar('T')
class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.__current: Node[T] | None = None
        self.__fin = False

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        new_node.next = self.__head
        self.__size += 1

    def preppend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__tail.next = self.__head
        self.__size += 1

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def shift(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacia")
        elif self.__head == self.__tail:
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            current = self.__head
            self.__head = self.__head.next
            self.__tail.next = self.__head
            current.next = None
            self.__size -= 1
            return current.data

    def pop(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacia")
        elif self.__head == self.__tail:
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            current = self.__tail
            previous = self.find_at(self.__size-2)
            current.next = None
            self.__tail = previous
            self.__tail.next = self.__head
            self.__size -= 1
            return current.data

    def find_at(self, index: int):
        current = self.__head

        for current_index in range(self.__size):
            if current_index == index:
                return current
            else:
                current = current.next

        raise IndexError("La pocicion no existe")

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.is_empty():
            print("La lista esta vacia")
            raise StopIteration
        if self.__fin:
            self.__fin = False
            raise StopIteration
        else:
            data = self.__current.data
            self.__current = self.__current.next
            if self.__current is self.__head:
                self.__fin = True
                return data
            return data
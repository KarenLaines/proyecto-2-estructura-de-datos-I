from __future__ import annotations
from typing import TypeVar, Generic, Optional
from node import Node


T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.size = 0

    def append(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def pop_first(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search(self, element: str) -> Optional[T]:
        current = self.head
        while current:
            if current.data.loan_id == element:
                return current.data
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


from __future__ import annotations
from typing import TypeVar, Generic, Optional
from node import Node


T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.size = 0

    # Agregar elementos al inicio ya l final
    def prepend(self, data: T):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node
        self.size += 1

    # Eliminar elementos al inicio y al final
    def pop_first(self):
        if self.head is None:
            return None
        else:
            node_to_remove= self.head
            self.head = self.head.next
            node_to_remove.next = None
            self.size -= 1
            return 'El nodo eliminado es: ', node_to_remove.data

    def pop(self):
        if self.head is None:
            raise IndexError('La lista está vacía')
        elif self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next

            data = current.next.data
            current.next = None
            self.size -= 1

            return data

    def search(self, element: str) -> Optional[T]:
        if self.head is None:
            return None
        else:
            element = element.strip()  # Eliminar espacios en blanco
            current = self.head
            while current is not None:
                if str(current.data).strip() == element:
                    return current.data
                current = current.next
            return None

    def display(self):
        if self.head is None:
            return 'La lista está vacía'
        else:
            current = self.head
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print('Elementos de la lista:')
            for element in elements:
                print(element)

            return elements


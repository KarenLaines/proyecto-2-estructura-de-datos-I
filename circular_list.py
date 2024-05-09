from node import Node
from typing import TypeVar, Generic, Optional


T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.__current: Node[T] | None = None
        self.__fin = False

# Insertar al inicio y al final
    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__tail.next = self.__head  # Asegurar conectividad circular
        self.__size += 1

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__tail.next = self.__head  # Mantener conectividad circular
        self.__size += 1

    # Eliminar al inicio y al final
    def pop_first(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacía")
        elif self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__tail.next = self.__head  # Mantener conexión circular
        self.__size -= 1

    def pop(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacía")
        elif self.__head == self.__tail:
            data = self.__head.data
            self.__head = None
            self.__tail = None
            self.__size = 0
            return data
        else:
            node_to_remove = self.__tail
            previous = self.find_at(self.__size-2)
            self.__tail = previous
            self.__tail.next = self.__head
            node_to_remove.next = None
            self.__size -= 1
            return node_to_remove.data

# Buscar valor
    def search(self, element: str) -> Optional [T]:
        if self.is_empty():
            return None  # La lista está vacía, no hay nada que buscar

        current = self.__head
        while True:
            if str(current.data).strip() == element:  # Compara el valor del nodo con el valor buscado
                return current  # Si se encuentra, devuelve el nodo

            current = current.next

            if current == self.__head:  # Si volvemos al principio, hemos recorrido la lista completa
                break

        return None  # Si no se encuentra, devuelve None

    # Rotar a la derecha y a la izquierda
    def right_rotation(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacía")
        current = self.__head
        while current.next != self.__tail:
            current = current.next
        self.__tail.next = self.__head
        self.__head = self.__tail
        self.__tail = current
        self.__tail.next = self.__head  # Mantener conexión circular

    def left_rotation(self):
        if self.is_empty():
            raise ReferenceError("La Lista esta vacía")

        elif self.__head == self.__tail:
            return self.__head.data

        current = self.__head.next

        self.__tail.next = self.__head
        self.__tail = self.__head

        self.__head = current
        self.__tail.next = self.__head


    def display(self):
        if self.is_empty():
            return "La lista está vacía"

        current = self.__head
        elements = []
        max_iterations = 2 * self.__size  # Seguridad adicional para evitar bucles infinitos

        for _ in range(max_iterations):
            elements.append(current.data)
            current = current.next

            if current is self.__head:
                break
        else:
            raise RuntimeError("Conectividad incorrecta en la lista circular")

        return elements

    # Métodos auxiliares

    def find_at(self, index: int):
        current = self.__head

        for current_index in range(self.__size):
            if current_index == index:
                return current
            else:
                current = current.next

        raise IndexError("La pocicion no existe")
    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.is_empty():
            print("La lista esta vacía")
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
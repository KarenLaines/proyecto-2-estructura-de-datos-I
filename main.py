from Doublelist import DoublyLinkedList
from CircularDoulelist import CircularDoublyLinkedList

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.print_list()  # Salida esperada: 0 1 2 3
    dll.delete(2)
    dll.print_list()  # Salida esperada: 0 1 3

    cdll = CircularDoublyLinkedList()
    cdll.append(1)
    cdll.append(2)
    cdll.append(3)
    cdll.prepend(0)
    cdll.print_list()  # Salida esperada: 0 1 2 3
    cdll.delete(2)
    cdll.print_list()  # Salida esperada: 0 1 3




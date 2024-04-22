from Doublelist import DoublyLinkedList

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.print_list()  # Salida esperada: 0 1 2 3
    dll.delete(2)
    dll.print_list()  # Salida esperada: 0 1 3


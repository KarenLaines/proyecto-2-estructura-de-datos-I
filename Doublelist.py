import tkinter as tk
from tkinter import simpledialog

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_at_beginning(data)
        elif position >= self.length():
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 2):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def delete_first_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        current = self.tail.prev
        current.next = None
        self.tail = current

    def delete_at_position(self, position):
        if position <= 0:
            self.delete_first_node()
        elif position >= self.length() -1:
            self.delete_last_node()
        else:
            current = self.head
            for _ in range(position-1):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            while current:
                file.write(str(current.data) + '\n')
                current = current.next

    def load_from_file(self, filename):
        self.head = None
        self.tail = None
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip()
                self.insert_at_end(data)

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class DoublyLinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Doubly Linked List")
        self.master.geometry("300x200")

        self.doubly_linked_list = DoublyLinkedList()

        self.label = tk.Label(master, text="Doubly Linked List")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insert_beginning_button = tk.Button(master, text="Insert Beginning", command=self.insert_beginning)
        self.insert_beginning_button.pack()

        self.insert_end_button = tk.Button(master, text="Insert End", command=self.insert_end)
        self.insert_end_button.pack()

        self.insert_position_button = tk.Button(master, text="Insert Position", command=self.insert_position)
        self.insert_position_button.pack()

        self.delete_first_button = tk.Button(master, text="Delete First", command=self.delete_first)
        self.delete_first_button.pack()

        self.delete_last_button = tk.Button(master, text="Delete Last", command=self.delete_last)
        self.delete_last_button.pack()

        self.delete_position_button = tk.Button(master, text="Delete Position", command=self.delete_position)
        self.delete_position_button.pack()

        self.display_label = tk.Label(master, text="Doubly Linked List:")
        self.display_label.pack()

        self.display_text = tk.Text(master, height=8, width=30)
        self.display_text.pack()

        self.display()

    def insert_beginning(self):
        data = self.entry.get()
        self.doubly_linked_list.insert_at_beginning(data)
        self.entry.delete(0, tk.END)
        self.display()

    def insert_end(self):
        data = self.entry.get()
        self.doubly_linked_list.insert_at_end(data)
        self.entry.delete(0, tk.END)
        self.display()

    def insert_position(self):
        data = self.entry.get()
        position = int(simpledialog.askstring("Position", "Enter position:"))
        self.doubly_linked_list.insert_at_position(data, position)
        self.entry.delete(0, tk.END)
        self.display()

    def delete_first(self):
        self.doubly_linked_list.delete_first_node()
        self.display()

    def delete_last(self):
        self.doubly_linked_list.delete_last_node()
        self.display()

    def delete_position(self):
        position = int(simpledialog.askstring("Position", "Enter position:"))
        self.doubly_linked_list.delete_at_position(position)
        self.display()

    def display(self):
        self.display_text.delete(1.0, tk.END)
        current = self.doubly_linked_list.head
        while current:
            self.display_text.insert(tk.END, str(current.data) + "\n")
            current = current.next

if __name__ == "__main__":
    root = tk.Tk()
    app = DoublyLinkedListGUI(root)
    root.mainloop()

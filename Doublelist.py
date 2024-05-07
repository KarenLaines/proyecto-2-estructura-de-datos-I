import tkinter as tk

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

        self.delete_button = tk.Button(master, text="Delete", command=self.delete)
        self.delete_button.pack()

        self.display_label = tk.Label(master, text="Doubly Linked List:")
        self.display_label.pack()

        self.display_text = tk.Text(master, height=10, width=30)
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

    def delete(self):
        data = self.entry.get()
        self.doubly_linked_list.delete_node(data)
        self.entry.delete(0, tk.END)
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
import tkinter as tk

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            if current.next == current:
                self.head = None
            else:
                next_node = current.next
                prev_node = current.prev
                next_node.prev = prev_node
                prev_node.next = next_node
                self.head = next_node
            return

        while current and current.data != data:
            current = current.next

        if current is None:
            return

        next_node = current.next
        prev_node = current.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            if current:
                while True:
                    file.write(str(current.data) + '\n')
                    current = current.next
                    if current == self.head:
                        break

    def load_from_file(self, filename):
        self.head = None
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip()
                self.insert_at_end(data)

class CircularDoublyLinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Circular Doubly Linked List")
        self.master.geometry("300x250")

        self.circular_doubly_linked_list = CircularDoublyLinkedList()

        self.label = tk.Label(master, text="Circular Doubly Linked List")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insert_beginning_button = tk.Button(master, text="Insert Beginning", command=self.insert_beginning)
        self.insert_beginning_button.pack()

        self.insert_end_button = tk.Button(master, text="Insert End", command=self.insert_end)
        self.insert_end_button.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.delete)
        self.delete_button.pack()



        self.display_label = tk.Label(master, text="Circular Doubly Linked List:")
        self.display_label.pack()

        self.display_text = tk.Text(master, height=10, width=30)
        self.display_text.pack()

        self.display()

    def insert_beginning(self):
        data = self.entry.get()
        self.circular_doubly_linked_list.insert_at_beginning(data)
        self.entry.delete(0, tk.END)
        self.display()

    def insert_end(self):
        data = self.entry.get()
        self.circular_doubly_linked_list.insert_at_end(data)
        self.entry.delete(0, tk.END)
        self.display()

    def delete(self):
        data = self.entry.get()
        self.circular_doubly_linked_list.delete_node(data)
        self.entry.delete(0, tk.END)
        self.display()

    def display(self):
        self.display_text.delete(1.0, tk.END)
        current = self.circular_doubly_linked_list.head
        if current:
            while True:
                self.display_text.insert(tk.END, str(current.data) + "\n")
                current = current.next
                if current == self.circular_doubly_linked_list.head:
                    break

if __name__ == "__main__":
    root = tk.Tk()
    app = CircularDoublyLinkedListGUI(root)
    root.mainloop()

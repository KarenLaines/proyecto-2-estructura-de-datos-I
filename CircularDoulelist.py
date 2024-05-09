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

    def delete_at_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last_node = self.head.prev
            second_node = self.head.next
            last_node.next = second_node
            second_node.prev = last_node
            self.head = second_node

    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last_node = self.head.prev
            second_last_node = last_node.prev
            second_last_node.next = self.head
            self.head.prev = second_last_node
    def find_node_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

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
        self.master.geometry("300x300")

        self.circular_doubly_linked_list = CircularDoublyLinkedList()

        self.label = tk.Label(master, text="Circular Doubly Linked List")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insert_beginning_button = tk.Button(master, text="Insert Beginning", command=self.insert_beginning)
        self.insert_beginning_button.pack()

        self.insert_end_button = tk.Button(master, text="Insert End", command=self.insert_end)
        self.insert_end_button.pack()

        self.delete_beginning_button = tk.Button(master, text="Delete Beginning", command=self.delete_beginning)
        self.delete_beginning_button.pack()

        self.delete_end_button = tk.Button(master, text="Delete End", command=self.delete_end)
        self.delete_end_button.pack()

        self.search_button = tk.Button(master, text="Find", command=self.find_value)
        self.search_button.pack()

        self.display_label = tk.Label(master, text="Circular Doubly Linked List:")
        self.display_label.pack()

        self.display_text = tk.Text(master, height=10, width=30)
        self.display_text.pack()

        self.move_left_button = tk.Button(master, text="Mover Izquierda", command=self.move_left)
        self.move_left_button.pack()

        self.move_right_button = tk.Button(master, text="Mover Derecha", command=self.move_right)
        self.move_right_button.pack()

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

    def delete_beginning(self):
        self.circular_doubly_linked_list.delete_at_beginning()
        self.display()

    def delete_end(self):
        self.circular_doubly_linked_list.delete_at_end()
        self.display()

    def find_value(self):
        value = self.entry.get()
        node = self.circular_doubly_linked_list.find_node_by_value(value)
        if node:
            self.highlight_node(node)
        else:
            tk.messagebox.showinfo("Info", f"Valor '{value}' no encontrado.")

    def highlight_node(self, node):
        self.display_text.tag_config("highlight", background="yellow")
        self.display_text.mark_set("highlight_start", "1.0")
        self.display_text.mark_set("highlight_end", "end")
        self.display_text.tag_remove("highlight", "highlight_start", "highlight_end")
        start_index = self.display_text.search(str(node.data), "highlight_start", "highlight_end")
        while start_index:
            end_index = f"{start_index}+{len(str(node.data))}c"
            self.display_text.tag_add("highlight", start_index, end_index)
            start_index = self.display_text.search(str(node.data), end_index, "highlight_end")

    def display(self):
        self.display_text.delete(1.0, tk.END)
        current = self.circular_doubly_linked_list.head
        if current:
            while True:
                self.display_text.insert(tk.END, str(current.data) + "\n")
                current = current.next
                if current == self.circular_doubly_linked_list.head:
                    break

    def move_left(self):
        if self.circular_doubly_linked_list.head:
            self.circular_doubly_linked_list.head = self.circular_doubly_linked_list.head.prev
            self.display()

    def move_right(self):
        if self.circular_doubly_linked_list.head:
            self.circular_doubly_linked_list.head = self.circular_doubly_linked_list.head.next
            self.display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CircularDoublyLinkedListGUI(root)
    root.mainloop()
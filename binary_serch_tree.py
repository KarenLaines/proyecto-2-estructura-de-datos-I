from typing import TypeVar
from node import Node
import tkinter as tk
import random

T = TypeVar('T')


class BinaryTree:
    def __init__(self):
        self.__root = None

    def insert(self, data: T):
        new_node = Node(data)

        if self.__root is None:
            self.__root = new_node

        else:
            self.insert_recuersivo(self.__root, new_node)

    def insert_recuersivo(self, node, new_node):
        if new_node.data > node.data:
            if node.right is None:
                node.right = new_node
            else:
                self.insert_recuersivo(node.right, new_node)

        elif new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.insert_recuersivo(node.left, new_node)

        else:
            print("El valor ya esta en el arbol")

    def recorridos(self):
        print("Inorden")
        self.__inorden(self.__root)

        print("Postorden")
        self.__postorden(self.__root)

        print("PreOrden")
        self.__preorden(self.__root)

    def __inorden(self, node):
        if node is not None:
            self.__inorden(node.left)
            print(node.data)
            self.__inorden(node.right)

    def __postorden(self, node):
        if node is not None:
            self.__postorden(node.left)
            self.__postorden(node.right)
            print(node.data)

    def __preorden(self, node):
        if node is not None:
            self.__preorden(node.right)
            print(node.data)
            self.__preorden(node.left)

    def serch(self, data):
        route = []
        self.__search_recursive(data=data, route=route, node=self.__root)
        print(" -> ".join(route))

    def __search_recursive(self, data, node: Node[T], route):
        if node is None:
            print("El valor no se encuentra en el arbol")
            return

        if node.data == data:
            print(node.data)
            route.append(f"Subarbol {node.data}")
            return

        if node.data < data:
            print(node.data)
            route.append(f"Subarbol {node.data}")
            self.__search_recursive(data, node.right, route)

        if node.data > data:
            print(node.data)
            route.append(f"Subarbol {node.data}")
            self.__search_recursive(data, node.left, route)

    def max(self):
        print("Maximo")
        return self.__max_recursive(self.__root)

    def __max_recursive(self, node):
        if node is not None:
            if node.right is None:
                return node.data
            else:
                return self.__max_recursive(node.right)

    def min(self):
        print("Minimo")
        return self.__min_recursive(self.__root)

    def __min_recursive(self, node):
        if node is not None:
            if node.left is None:
                return node.data
            else:
                return self.__min_recursive(node.left)

    def height(self) -> int:
        print(self.__height_recursive(self.__root))
        return self.__height_recursive(self.__root)

    def __height_recursive(self, node: Node[T]) -> int:
        if node is None:
            return 0
        else:
            return 1 + max(self.__height_recursive(node.left), self.__height_recursive(node.right))

    def main(self):
        root = tk.Tk()
        root.title("Árbol Binario")

        self.actions(root)

        canvas = tk.Canvas(root, width=1800, height=1600)
        canvas.grid(row=0, column=1)

        self.draw_tree_recursive(canvas=canvas, node=self.__root, x=900, y=50, x_dist=200, y_dist=100)
        root.mainloop()

    def draw_tree_recursive(self, canvas, node, x, y, x_dist, y_dist):
        if node is None:
            return
        # Dibujar el nodo
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
        canvas.create_text(x, y, text=str(node.data), fill="white")
        # Dibujar las ramas izquierda y derecha
        if node.left:
            x_left = x - x_dist
            y_left = y + y_dist
            canvas.create_line(x, y, x_left, y_left)
            self.draw_tree_recursive(canvas, node.left, x_left, y_left, x_dist * 0.7, y_dist)
        if node.right:
            x_right = x + x_dist
            y_right = y + y_dist
            canvas.create_line(x, y, x_right, y_right)
            self.draw_tree_recursive(canvas, node.right, x_right, y_right, x_dist * 0.7, y_dist)

    def actions(self, root):
        def on_entry_click(event):
            if entry.get() == 'Ingrese valor a...':
                entry.delete(0, "end")  # Borra el texto actual en el cuadro de texto
                entry.insert(0, '')  # Inserta texto vacío para que el usuario pueda escribir
                entry.config(fg='black', font=('Courier', 20))  # Cambia el color del texto a negro

        def on_focusout(event):
            if entry.get() == '':
                entry.insert(0, 'Ingrese valor a...')
                entry.config(fg='grey', font=('Courier', 20))  # Cambia el color del texto a gris

        frame_buttons = tk.Frame(root)

        entry = tk.Entry(frame_buttons, font=('Courier', 20))
        entry.insert(0, 'Ingrese valor a...')
        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focusout)

        button_insert = tk.Button(frame_buttons, text="INSERTAR", font=('Courier', 15),
                                  command=lambda: self.insert(entry.get()))
        button_delete = tk.Button(frame_buttons, text="ELIMINAR", font=('Courier', 15))
        button_serch = tk.Button(frame_buttons, text="BUSCAR", font=('Courier', 15))

        entry.pack(fill='both', padx=5, pady=15)
        button_insert.pack(fill='both', padx=5, pady=5)
        button_delete.pack(fill='both', padx=5, pady=5)
        button_serch.pack(fill='both', padx=5, pady=5)

        frame_buttons.grid(row=0, column=0, sticky="nsew")


a = BinaryTree()

for i in range(40):
    a.insert(random.randint(0, 500))

a.main()

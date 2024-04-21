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

    def draw_tree(self):
        root = tk.Tk()
        root.title("Árbol Binario")

        canvas = tk.Canvas(root, width=5000, height=5000)
        canvas.pack()

        self.draw_tree_recursive(canvas=canvas, node=self.__root, x=400, y=50, x_dist=200, y_dist=100)
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
            self.draw_tree_recursive(canvas, node.left, x_left, y_left, x_dist / 2, y_dist)
        if node.right:
            x_right = x + x_dist
            y_right = y + y_dist
            canvas.create_line(x, y, x_right, y_right)
            self.draw_tree_recursive(canvas, node.right, x_right, y_right, x_dist / 2, y_dist)


a = BinaryTree()

for i in range(50):
    a.insert(random.randint(0, 500))

a.draw_tree()
a.recorridos()
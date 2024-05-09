from typing import TypeVar
from node_binary_serch_tree import Node
import tkinter as tk
import copy
from tkinter import messagebox
from tkinter import filedialog

T = TypeVar('T')


class BinaryTree:
    def __init__(self):
        self.__root = None

    def delete(self, data):
        self.__delete_recursive(self.__root, self.__root, data)

    def __delete_recursive(self, node: Node[T], father_node: Node[T], data):
        if node is None:
            print("El valor no se encuentra en el arbol")
            return

        elif node.data == data:
            if node.is_leaf():
                # Eliminacion de un nodo hoja
                if father_node.right is node:
                    father_node.right = None
                    node: None
                elif father_node.left is node:
                    father_node.left = None
                    node: None

            # Eliminacion de un nodo con un solo hijo
            elif node.right is None or node.left is None:
                if father_node.right is node:
                    if node.left is not None:
                        father_node.right = node.left
                    else:
                        father_node.right = node.right

                elif father_node.left is node:
                    if node.left is not None:
                        father_node.left = node.left
                    else:
                        father_node.left = node.right

            # Eliminacion de un nodo con dos hijos
            elif node.right is not None and node.left is not None:
                max_node = self.__max_recursive(node.left)
                max_copie = copy.deepcopy(max_node)
                self.delete(max_node.data)

                if father_node.right is node:
                    father_node.right.data = max_copie.data
                elif father_node.left is node:
                    father_node.left.data = max_copie.data
                elif father_node is node:
                    father_node.data = max_copie.data
            return

        elif node.data < data:
            self.__delete_recursive(node.right, node, data)

        elif node.data > data:
            self.__delete_recursive(node.left, node, data)

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
            raise TypeError

    def recorridos(self):
        print("Inorden")
        self.__inorden(self.__root, [])

        print("Postorden")
        self.__postorden(self.__root)

        print("PreOrden")
        self.__preorden(self.__root)

    def __inorden(self, node, lista: []):
        if node is not None:
            self.__inorden(node.left, lista)
            lista.append(node.data)
            self.__inorden(node.right, lista)
        else:
            return lista

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
                return node
            else:
                return self.__max_recursive(node.right)

    def min(self):
        print("Minimo")
        return self.__min_recursive(self.__root)

    def __min_recursive(self, node):
        if node is not None:
            if node.left is None:
                return node
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

        canvas = tk.Canvas(root, width=1500, height=900)
        canvas.grid(row=0, column=1)

        self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
        root.mainloop()

    def draw_tree_recursive(self, canvas, node, x, y, x_dist, y_dist):
        if node is None:
            return
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

            # Obtener las dimensiones del texto
        text_width = canvas.bbox(canvas.create_text(0, 0, text=str(node.data), font=('Courier', 15)))[2]
        text_height = canvas.bbox(canvas.create_text(0, 0, text=str(node.data), font=('Courier', 15)))[3]

        # Dibujar el nodo
        canvas.create_oval(x - text_width * 0.8 - 10, y - text_height * 0.8 - 10, x + text_width * 0.8 + 10,
                           y + text_height * 0.8 + 10, fill="lightblue")
        canvas.create_text(x, y, text=str(node.data), fill="black", font=('Courier', 15))

    def actions(self, root):
        def exportt():
            lista = []
            self.__inorden(self.__root, lista)

            # Mostrar el cuadro de diálogo para seleccionar la ubicación de destino
            ubicacion_destino = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Archivos de texto", "*.txt")])
            if ubicacion_destino:
                # Escribir el contenido en el archivo de destino
                with open(ubicacion_destino, 'w') as file:
                    for i in lista:
                        file.write(f"{i} ")
                print(f"Archivo exportado correctamente a: {ubicacion_destino}")

        def imppp():
            archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

            with open(archivo, "r") as fichero:

                # Recorremos las lineas de cada fichero
                for linea in fichero.readlines():

                    # Obtenemos las palabras de cada fichero
                    for palabra in linea.split():
                        self.insert(palabra)

            canvas = tk.Canvas(root, width=1500, height=900)
            canvas.grid(row=0, column=1)
            self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)

        def insssss():
            try:
                self.insert(get_entry())
                messagebox.showinfo("EXITO", "El nodo ha sido agregado con exito")

                canvas = tk.Canvas(root, width=1500, height=900)
                canvas.grid(row=0, column=1)
                self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
            except TypeError:
                messagebox.showinfo("FRACASO", "El nodo no ha sido agregado con exito")

        def delll():
            try:
                self.delete(get_entry())
                messagebox.showinfo("EXITO", "El nodo ha sido eliminado con exito")
                canvas = tk.Canvas(root, width=1500, height=900)
                canvas.grid(row=0, column=1)

                self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
            except TypeError:
                messagebox.showinfo("FRACASO", "El nodo no ha sido eliminado con exito")

        def seeerch():
            try:
                route = []
                self.__search_recursive(data=get_entry(), route=route, node=self.__root)
                messagebox.showinfo("EXITO", "Este es el recorrido: " + " -> ".join(route))

            except TypeError:
                messagebox.showinfo("FRACASO", "El nodo no ha sido encontrado")

        def get_entry():
            try:
                ins = int(entry.get())
            except ValueError:
                ins = entry.get()
            return ins

        def on_entry_click(event):
            if entry.get() == 'Ingrese valor a...':
                entry.delete(0, "end")  # Borra el texto actual en el cuadro de texto
                entry.insert(0, '')  # Inserta texto vacío para que el usuario pueda escribir
                entry.config(fg='black', font=('Courier', 20))  # Cambia el color del texto a negro

        def on_focusout(event):
            if entry.get() == '':
                entry.insert(0, 'Ingrese valor a...')
                entry.config(fg='grey', font=('Courier', 20))  # Cambia el color del texto a gris

        frame_buttons = tk.Frame(root, bg="lightblue")

        entry = tk.Entry(frame_buttons, font=('Courier', 20))
        entry.insert(0, 'Ingrese valor a...')
        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focusout)

        button_insert = tk.Button(frame_buttons, text="INSERTAR", font=('Courier', 15),
                                  command=lambda: insssss())
        button_delete = tk.Button(frame_buttons, text="ELIMINAR", font=('Courier', 15),
                                  command=lambda: delll())
        button_serch = tk.Button(frame_buttons, text="BUSCAR", font=('Courier', 15),
                                 command=lambda: seeerch())
        button_export = tk.Button(frame_buttons, text="EXPORTAR", font=('Courier', 15), command=exportt)
        button_import = tk.Button(frame_buttons, text="IMPORTAR", font=('Courier', 15), command=imppp)

        entry.pack(fill='both', padx=30, pady=30)
        button_insert.pack(fill='both', padx=30, pady=5)
        button_delete.pack(fill='both', padx=30, pady=5)
        button_serch.pack(fill='both', padx=30, pady=5)

        button_import.pack(fill='both', padx=30, pady=5, side='bottom')
        button_export.pack(fill='both', padx=30, pady=5, side='bottom')

        frame_buttons.grid(row=0, column=0, sticky="nsew", columnspan=True)

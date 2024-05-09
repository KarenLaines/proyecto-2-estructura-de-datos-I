from typing import Optional, Generic
from typing import TypeVar
from node_binary_serch_tree import Node
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self.__root: Node[T] | None = None

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

        def insssss_left():
            try:
                if self.__root is not None:
                    self.insert_left(get_entry(), get_entry_reft())
                    messagebox.showinfo("EXITO", "El nodo ha sido agregado con exito")

                    canvas = tk.Canvas(root, width=1500, height=900)
                    canvas.grid(row=0, column=1)
                    self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
                else:
                    self.insert(get_entry())
                    canvas = tk.Canvas(root, width=1500, height=900)
                    canvas.grid(row=0, column=1)
                    self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
            except ValueError:
                messagebox.showinfo("FRACASO", "El nodo no ha sido agregado con exito")

        def inssss_right():
            try:
                if self.__root is not None:
                    self.insert_right(get_entry(), get_entry_reft())
                    messagebox.showinfo("EXITO", "El nodo ha sido agregado con exito")

                    canvas = tk.Canvas(root, width=1500, height=900)
                    canvas.grid(row=0, column=1)
                    self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)
                elif self.__root is None:
                    self.insert(get_entry())
            except ValueError:
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
                canvas = tk.Canvas(root, width=1500, height=900)
                canvas.grid(row=0, column=1)
                self.draw_tree_recursive(canvas=canvas, node=self.__root, x=750, y=50, x_dist=200, y_dist=100)

        def seeerch():
            try:
                route = []
                self.search_by_value(data=get_entry(), node=self.__root, lista=route)
                messagebox.showinfo("EXITO", "Este es el recorrido: " + " -> ".join(route))

            except TypeError:
                messagebox.showinfo("FRACASO", "El nodo no ha sido encontrado")

        def get_entry():
            try:
                ins = int(entry.get())
            except ValueError:
                ins = entry.get()
            return ins

        def get_entry_reft():
            try:
                ins = int(entry_referencia.get())
            except ValueError:
                ins = entry_referencia.get()
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

        def on_entry_click_referencia(event):
            if entry_referencia.get() == 'Ingrese valor referencia...':
                entry_referencia.delete(0, "end")  # Borra el texto actual en el cuadro de texto
                entry_referencia.insert(0, '')  # Inserta texto vacío para que el usuario pueda escribir
                entry_referencia.config(fg='black', font=('Courier', 20))  # Cambia el color del texto a negro

        def on_focusout_referencia(event):
            if entry_referencia.get() == '':
                entry_referencia.insert(0, 'Ingrese valor referencia...')
                entry_referencia.config(fg='grey', font=('Courier', 20))  # Cambia el color del texto a gris

        frame_buttons = tk.Frame(root, bg="lightblue")

        entry = tk.Entry(frame_buttons, font=('Courier', 20))
        entry.insert(0, 'Ingrese valor a...')
        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focusout)

        entry_referencia = tk.Entry(frame_buttons, font=('Courier', 20))
        entry_referencia.insert(0, 'Ingrese valor referencia...')
        entry_referencia.bind('<FocusIn>', on_entry_click_referencia)
        entry_referencia.bind('<FocusOut>', on_focusout_referencia)

        button_insert_left = tk.Button(frame_buttons, text="INSERTAR A LA IZQUIERDA", font=('Courier', 15),
                                       command=lambda: insssss_left())
        button_insert_right = tk.Button(frame_buttons, text="INSERTAR A LA DERECHA", font=('Courier', 15),
                                        command=lambda: inssss_right())
        button_delete = tk.Button(frame_buttons, text="ELIMINAR", font=('Courier', 15),
                                  command=lambda: delll())
        button_serch = tk.Button(frame_buttons, text="BUSCAR", font=('Courier', 15),
                                 command=lambda: seeerch())
        button_export = tk.Button(frame_buttons, text="EXPORTAR", font=('Courier', 15), command=exportt)
        button_import = tk.Button(frame_buttons, text="IMPORTAR", font=('Courier', 15), command=imppp)

        entry_referencia.pack(fill='both', padx=30, pady=30)
        entry.pack(fill='both', padx=30, pady=30)
        button_insert_left.pack(fill='both', padx=30, pady=5)
        button_insert_right.pack(fill='both', padx=30, pady=5)
        button_delete.pack(fill='both', padx=30, pady=5)
        button_serch.pack(fill='both', padx=30, pady=5)

        button_import.pack(fill='both', padx=30, pady=5)
        button_export.pack(fill='both', padx=30, pady=5)

        frame_buttons.grid(row=0, column=0, sticky="nsew", columnspan=True)

    # FUNCION  PARA CALCULAR LA ALTURA DEL ARBOl
    def altura(self, subtree: Node[T]):

        if subtree is None:
            return 0

        return 1 + max(self.altura(subtree.left), self.altura(subtree.right))

    def insert_left(self, data, ref=None):
        if ref is None:
            if self.__root is None:
                self.__root = Node(data)
                print("Nuevo nodo establecido como raíz.")
            else:
                raise ValueError("El árbol ya tiene una raíz. Especifique un nodo de referencia para insertar.")
        else:
            parent_node = self.search(ref, self.__root)
            if parent_node is not None:
                if parent_node.left is None:
                    parent_node.left = Node(data)
                    print(f"Nodo insertado a la izquierda de {ref}.")
                else:
                    raise ValueError("El nodo ya tiene un hijo izquierdo.")
            else:
                raise ValueError("Nodo de referencia no encontrado.")

    def insert_right(self, data, ref=None):
        if ref is None:
            raise ValueError("Debe especificar un nodo de referencia para insertar a la derecha.")
        else:
            parent_node = self.search(ref, self.__root)
            if parent_node is not None:
                if parent_node.right is None:
                    parent_node.right = Node(data)
                    print(f"Nodo insertado a la derecha de {ref}.")
                else:
                    raise ValueError("El nodo ya tiene un hijo derecho.")
            else:
                raise ValueError("Nodo de referencia no encontrado.")

    def search_by_value(self, data, node, path=None, lista=[]):
        if node is None:
            return None
        if path is None:
            path = []  # Inicializa la lista de camino solo en la primera llamada

        path.append(node)  # Agregar el objeto nodo actual al camino
        lista.append(f"Visitando nodo: {node.data}, camino actual: {[n.data for n in path]}")

        # Verificar si el nodo actual contiene el dato buscado
        if int(node.data) == int(data):
            lista.append(f"Dato encontrado: {data} en el nodo {node.data}, camino final: {[n.data for n in path]}")
            return node, path  # Devuelve el nodo y el camino recorrido hasta él

        # Búsqueda en el subárbol izquierdo
        left_result = None
        if node.left is not None:
            lista.append(f"Buscando a la izquierda de {node.data}")
            left_result = self.search_by_value(data, node.left, path)
            if left_result is not None:
                return left_result

        # Búsqueda en el subárbol derecho
        right_result = None
        if node.right is not None:
            lista.append(f"Buscando a la derecha de {node.data}")
            right_result = self.search_by_value(data, node.right, path)
            if right_result is not None:
                return right_result

        # Si el nodo no es encontrado en ninguno de los subárboles y no es el nodo buscado, remover del camino
        if left_result is None and right_result is None:
            path.pop()  # Solo quitar el último nodo añadido si no condujo al nodo buscado
            lista.append(f"Nodo {node.data} no contiene el dato y no fue encontrado en sus subárboles, removiendo de "
                         f"camino.")

        return None

    def search(self, data, node):
        if node is None:
            return None
        elif node.data == data:
            return node
        else:
            left_result = self.search(data, node.left)
            if left_result is not None:
                return left_result
            return self.search(data, node.right)

    def is_empty(self) -> bool:
        return self.__root is None

    def __preorder(self, subtree: Node[T] | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)
            left = self.__preorder(subtree.left)
            right = self.__preorder(subtree.right)
            result = f"{root}({left},{right})"
            return result

    def preorder(self):
        return self.__preorder(self.__root)

    def __inorden(self, node, lista: []):
        if node is not None:
            self.__inorden(node.left, lista)
            lista.append(node.data)
            self.__inorden(node.right, lista)
        else:
            return lista

    def inorden(self):
        return self.__inorden(self.__root, [])

    def __postorden(self, subtree: Node[T] | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)
            left = self.__postorden(subtree.left)
            right = self.__postorden(subtree.right)
            result = f"{left}({right},{root})"
            return result

    def postorden(self):
        return self.__postorden(self.__root)

    def get_path(self, ref: T, subtree: Node[T] | None) -> str:
        if subtree is None:
            return ""
        else:
            root = subtree.data
            if root == ref:
                return root

            left = self.get_path(ref, subtree.left)

            if left != "":
                return f"left --> {left}"

            rigth = self.get_path(ref, subtree.right)

            if rigth != "":
                return f"rigth --> {rigth}"
            else:
                return ""

    def get_path_data(self, ref: T, subtree: Node[T] | None) -> str:
        path = self._get_path_helper(ref, subtree)
        if path:
            return " --> ".join(map(str, path))
        else:
            return "Valor no encontrado en el árbol."

    def _get_path_helper(self, ref: T, subtree: Node[T] | None, path: list = None) -> list:
        if path is None:
            path = []
        if subtree is None:
            return []
        elif subtree.data == ref:
            # Añade el valor actual al camino y retorna el camino
            return path + [subtree.data]
        else:
            # Prueba primero por la izquierda
            left_path = self._get_path_helper(ref, subtree.left, path + [subtree.data])
            if left_path:
                return left_path

            # Si no se encontró por la izquierda, prueba por la derecha
            right_path = self._get_path_helper(ref, subtree.right, path + [subtree.data])
            if right_path:
                return right_path

            # Si no se encontró el valor, retorna una lista vacía
            return []

    def insert(self, data: T):
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursive(self.__root, data)

    def _insert_recursive(self, node: Node[T], data: T):
        comp_result = Node.compare(data, node.data)
        if comp_result < 0:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif comp_result > 0:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def print_tree(self, node=None, prefix=""):
        if node is None:
            node = self.__root
        if node is not None:
            if node.right is not None:
                self.print_tree(node.right, prefix + "    ")
            print(prefix + "-> " + str(node.data))
            if node.left is not None:
                self.print_tree(node.left, prefix + "    ")

    def search_min_node(self, subtree):
        if subtree is None:
            return None

        # Recursivamente busca el nodo con el valor mínimo en el subárbol izquierdo
        if subtree.left is not None:
            return self.search_min_node(subtree.left)

        # Si no hay más nodos a la izquierda, este es el nodo con el valor mínimo
        return subtree

    def search_max(self, subtree):
        # Caso base: Si el nodo es None, simplemente retornar None
        if subtree is None:
            return None

        # Comenzar asumiendo que el nodo actual es el máximo
        node_maximo = subtree

        # Buscar recursivamente el nodo máximo en el subárbol izquierdo
        if subtree.left is not None:
            left_max_node = self.search_max(subtree.left)
            if left_max_node is not None and left_max_node.data > node_maximo.data:
                node_maximo = left_max_node

        # Buscar recursivamente el nodo máximo en el subárbol derecho
        if subtree.right is not None:
            right_max_node = self.search_max(subtree.right)
            if right_max_node is not None and right_max_node.data > node_maximo.data:
                node_maximo = right_max_node

        # Devolver el nodo que contiene el valor máximo encontrado
        return node_maximo

    def delete(self, data: T) -> bool:
        self.__root, deleted = self._delete_recursive(self.__root, data)
        return deleted

    def _delete_recursive(self, subtree: Node, data) -> tuple[Optional[Node], bool]:
        if subtree is None:
            # Si el subárbol está vacío, no hay nada que eliminar
            return None, False

        if data == subtree.data:
            # Nodo encontrado
            if subtree.left is None and subtree.right is None:
                # El nodo es una hoja
                return None, True
            elif subtree.left is None:
                # Solo tiene hijo derecho
                return subtree.right, True
            elif subtree.right is None:
                # Solo tiene hijo izquierdo
                return subtree.left, True
            else:
                # Tiene dos hijos
                max_node = self.search_max(subtree.left)
                subtree.data = max_node.data  # Asegúrate que max_node es un Nodo y no un entero
                subtree.left, _ = self._delete_recursive(subtree.left, max_node.data)
                return subtree, True
        else:
            # Continuar búsqueda en los subárboles
            subtree.left, deleted_left = self._delete_recursive(subtree.left, data)
            subtree.right, deleted_right = self._delete_recursive(subtree.right, data)
            return subtree, deleted_left or deleted_right

    def insert_into_tree(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.data:
                root.left = self.insert_into_tree(root.left, key)
            else:
                root.right = self.insert_into_tree(root.right, key)
        return root

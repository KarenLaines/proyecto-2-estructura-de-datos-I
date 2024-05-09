import tkinter as tk
import random
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
from fpdf import FPDF

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

class Stack:
    def __init__(self, limit: int | None = None):
        self.size = 0
        self.max = limit
        self.head: Node | None = None

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, data: int):
        if self.max is not None and self.size == self.max:
            raise OverflowError("Desbordamiento de pila")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Subdesbordamiento de pila")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def search(self, target: int) -> int:
        current = self.head
        position = 1
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

class Ventana:
    def __init__(self, estructura):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("PILA")

        # Frame principal
        self.frame_principal = tk.Frame(self.ventana_principal)
        self.frame_principal.pack()

        # Frame para la visualización de la pila y el scroll
        self.frame_canvas = tk.Frame(self.frame_principal)
        self.frame_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_canvas, width=400, height=400)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame_canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame para los botones y entrys
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(side=tk.RIGHT, padx=10)

        self.estructura = estructura

        self.entry_agregar = tk.Entry(self.frame_controles, bg="#d3d3d3")
        self.entry_agregar.pack(pady=5)

        self.agregar_button = tk.Button(self.frame_controles, text="Agregar elemento", command=self.agregar_elemento, bg="#d3d3d3")
        self.agregar_button.pack(pady=5)

        self.quitar_button = tk.Button(self.frame_controles, text="Quitar elemento", command=self.quitar_elemento, bg="#d3d3d3")
        self.quitar_button.pack(pady=5)

        self.entry_buscar = tk.Entry(self.frame_controles, bg="#d3d3d3")
        self.entry_buscar.pack(pady=5)

        self.buscar_button = tk.Button(self.frame_controles, text="Buscar elemento", command=self.buscar_elemento, bg="#d3d3d3")
        self.buscar_button.pack(pady=5)

        self.importar_button = tk.Button(self.frame_controles, text="Importar desde archivo PDF", command=self.importar_desde_pdf, bg="#d3d3d3")
        self.importar_button.pack(pady=5)

        self.exportar_button = tk.Button(self.frame_controles, text="Exportar a PDF", command=self.exportar_a_pdf, bg="#d3d3d3")
        self.exportar_button.pack(pady=5)

        self.explicacion_label = tk.Label(self.frame_controles, text="Explicación:", bg="#d3d3d3")
        self.explicacion_label.pack(pady=5)

        self.explicacion_text = tk.Text(self.frame_controles, width=50, height=5, bg="#d3d3d3")
        self.explicacion_text.pack(pady=5)

        self.mostrar_estructura()
        self.actualizar_explicacion()

        self.ventana_principal.mainloop()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def mostrar_estructura(self):
        self.canvas.delete("all")
        if isinstance(self.estructura, Stack):
            self.mostrar_pila()

    def mostrar_pila(self):
        nodo_actual = self.estructura.head
        x = 200
        y = 20
        while nodo_actual is not None:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.canvas.create_rectangle(x - 30, y, x + 30, y + 30, outline="black", fill=color)
            self.canvas.create_text(x, y + 15, text=str(nodo_actual.data))
            if nodo_actual.next:
                self.canvas.create_line(x, y + 30, x, y + 55, arrow=tk.LAST)
            y += 50
            nodo_actual = nodo_actual.next


    def actualizar_explicacion(self):
        explicacion_general = (
            "Una pila es una estructura de datos lineal que sigue el principio LIFO (Last In, First Out),\n"
            "lo que significa que el último elemento agregado es el primero en ser eliminado.\n\n"
            "Operaciones básicas:\n"
            "- Push: Añade un elemento a la pila.\n"
            "- Pop: Elimina el elemento más reciente de la pila.\n"
            "- Search: Busca un elemento en la pila y devuelve su posición.\n\n"
            "En esta interfaz, puedes agregar elementos a la pila, quitar elementos, buscar elementos y exportar\n"
            "la visualización de la pila a un archivo PDF."
        )
        self.explicacion_text.delete("1.0", tk.END)
        self.explicacion_text.insert(tk.END, explicacion_general)

    def agregar_elemento(self):
        elemento = self.entry_agregar.get()
        if elemento:
            if isinstance(self.estructura, Stack):
                self.estructura.push(int(elemento))
            self.mostrar_estructura()
            self.actualizar_explicacion()
            self.entry_agregar.delete(0, tk.END)

    def quitar_elemento(self):
        try:
            if isinstance(self.estructura, Stack):
                self.estructura.pop()
            self.mostrar_estructura()
            self.actualizar_explicacion()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def buscar_elemento(self):
        elemento = self.entry_buscar.get()
        if elemento:
            position = self.estructura.search(int(elemento))
            if position != -1:
                messagebox.showinfo("Buscar elemento", f"El elemento {elemento} está en la posición {position} de la pila.")
            else:
                messagebox.showinfo("Buscar elemento", f"El elemento {elemento} no está en la pila.")
            self.entry_buscar.delete(0, tk.END)

    def importar_desde_pdf(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if filename:
            try:
                doc = fitz.open(filename)
                text = ""
                for page in doc:
                    text += page.get_text()
                stack = Stack()
                for item in text.split():
                    if item.isdigit():
                        stack.push(int(item))
                self.estructura = stack
                self.mostrar_estructura()
                self.actualizar_explicacion()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def exportar_a_pdf(self):
        # El código para exportar la pila a un PDF permanece igual
        pass


if __name__ == "__main__":
    pila = Stack()
    ventana_pila = Ventana(pila)

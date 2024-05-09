import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # Importar fitz (PyMuPDF)
import random  # Importar random

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

class Queue:
    def __init__(self, max_size: int | None = None):
        self.size = 0
        self.max_size = max_size
        self.front: Node | None = None
        self.rear: Node | None = None

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.max_size is not None and self.size == self.max_size

    def enqueue(self, data: int):
        if self.is_full():
            raise OverflowError("Desbordamiento de cola")
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Subdesbordamiento de cola")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def search(self, target: int) -> int:
        current = self.front
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
        self.ventana_principal.title("COLA")

        # Frame principal
        self.frame_principal = tk.Frame(self.ventana_principal)
        self.frame_principal.pack()

        # Frame para la visualización de la cola y el scroll
        self.frame_canvas = tk.Frame(self.frame_principal)
        self.frame_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_canvas, width=400, height=400)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame_canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        # Frame para los botones y entrys
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(side=tk.BOTTOM, padx=10)

        self.estructura = estructura

        self.entry_agregar = tk.Entry(self.frame_controles, bg="#d3d3d3")
        self.entry_agregar.pack(pady=5)

        self.agregar_button = tk.Button(self.frame_controles, text="Encolar elemento", command=self.encolar_elemento, bg="#d3d3d3")
        self.agregar_button.pack(pady=5)

        self.desencolar_button = tk.Button(self.frame_controles, text="Desencolar elemento", command=self.desencolar_elemento, bg="#d3d3d3")
        self.desencolar_button.pack(pady=5)

        self.entry_buscar = tk.Entry(self.frame_controles, bg="#d3d3d3")
        self.entry_buscar.pack(pady=5)

        self.buscar_button = tk.Button(self.frame_controles, text="Buscar elemento", command=self.buscar_elemento, bg="#d3d3d3")
        self.buscar_button.pack(pady=5)

        self.exportar_button = tk.Button(self.frame_controles, text="Exportar a PDF", command=self.exportar_a_pdf, bg="#d3d3d3")
        self.exportar_button.pack(pady=5)

        self.importar_button = tk.Button(self.frame_controles, text="Importar desde archivo", command=self.importar_desde_archivo, bg="#d3d3d3")
        self.importar_button.pack(pady=5)

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
        if isinstance(self.estructura, Queue):
            self.mostrar_cola()

    def mostrar_cola(self):
        nodo_actual = self.estructura.front
        x = 20
        y = 200
        while nodo_actual is not None:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.canvas.create_rectangle(x, y - 20, x + 20, y + 20, outline="black", fill=color)
            self.canvas.create_text(x + 10, y, text=str(nodo_actual.data))
            if nodo_actual.next:
                self.canvas.create_line(x + 20, y, x + 40, y, arrow=tk.LAST)
            x += 40
            nodo_actual = nodo_actual.next

    def actualizar_explicacion(self):
        explicacion_general = (
            "Una cola es una estructura de datos lineal que sigue el principio FIFO (First In, First Out),\n"
            "lo que significa que el primer elemento encolado es el primero en ser desencolado.\n\n"
            "Operaciones básicas:\n"
            "- Enqueue: Añade un elemento a la cola.\n"
            "- Dequeue: Elimina el primer elemento de la cola.\n"
            "- Search: Busca un elemento en la cola y devuelve su posición.\n\n"
            "En esta interfaz, puedes encolar elementos, desencolar elementos, buscar elementos y exportar\n"
            "la visualización de la cola a un archivo PDF."
        )
        self.explicacion_text.delete("1.0", tk.END)
        self.explicacion_text.insert(tk.END, explicacion_general)

    def encolar_elemento(self):
        elemento = self.entry_agregar.get()
        if elemento:
            if isinstance(self.estructura, Queue):
                self.estructura.enqueue(int(elemento))
            self.mostrar_estructura()
            self.actualizar_explicacion()
            self.entry_agregar.delete(0, tk.END)

    def desencolar_elemento(self):
        try:
            if isinstance(self.estructura, Queue):
                self.estructura.dequeue()
            self.mostrar_estructura()
            self.actualizar_explicacion()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def buscar_elemento(self):
        elemento = self.entry_buscar.get()
        if elemento:
            position = self.estructura.search(int(elemento))
            if position != -1:
                messagebox.showinfo("Buscar elemento", f"El elemento {elemento} está en la posición {position} de la cola.")
            else:
                messagebox.showinfo("Buscar elemento", f"El elemento {elemento} no está en la cola.")
            self.entry_buscar.delete(0, tk.END)

    def exportar_a_pdf(self):
        # Este método permanece igual
        pass

    def importar_desde_archivo(self):
        filename = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if filename:
            try:
                doc = fitz.open(filename)
                text = ""
                for page in doc:
                    text += page.get_text()
                self.estructura = Queue()
                for item in text.split():
                    if item.isdigit():
                        self.estructura.enqueue(int(item))
                self.mostrar_estructura()
                self.actualizar_explicacion()
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    cola = Queue()
    ventana_cola = Ventana(cola)

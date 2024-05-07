import tkinter as tk
from tkinter import messagebox
from main import linked_list
from main import circular_list


window = tk.Tk()
window.geometry("400x400")
window.title("GESTIÓN DE LISTAS")

main_menu_frame = tk.Frame(window)
main_menu_frame.pack(padx=20, pady=20)


# LISTA ENLAZADA

# Botón de prepend
def show_linked_list_menu():
    submenu = tk.Toplevel(window)
    submenu.title("Lista Enlazada")
    submenu.geometry("700x600")

    prepend_button = tk.Button(submenu, text="Agregar elemento al inicio", command=lambda: (add_to_front()),
                               bg='light blue', width=25, height=2, fg='blue')
    append_button = tk.Button(submenu, text="Agregar elemento al final", command=lambda: (add_to_end()),
                              bg='light blue', width=25, height=2, fg='blue')
    search_button = tk.Button(submenu, text="Buscar elemento", command=lambda: (search_element(element_to_search)),
                              bg='light blue', width=25, height=2, fg='blue')

    element_to_prepend = tk.Entry(submenu)
    element_to_prepend.grid(row=0, column=0, padx=100, pady=50)

    element_to_append = tk.Entry(submenu)
    element_to_append.grid(row=1, column=0, padx=50, pady=20)

    element_to_search = tk.Entry(submenu)
    element_to_search.grid(row=4, column=0, padx=50, pady=20)

    def add_to_front():
        data = element_to_prepend.get()
        linked_list.prepend(data)
        display_list()

    def add_to_end():
        data = element_to_append.get()
        linked_list.append(data)
        display_list()

    # En el código de Tkinter, antes de buscar
    def search_element(entry):
        data = entry.get().strip()  # Obtener el texto del Entry
        result = linked_list.search(data)  # Buscar en la lista

        if result is not None:
            messagebox.showinfo("Búsqueda exitosa", f"Elemento '{data}' está en la lista.")
        else:
            messagebox.showinfo("Elemento no encontrado", f"Elemento '{data}' no está en la lista.")

        # Verifica la lista para asegurarte de que los datos son correctos
        linked_list.display()

    def display_list():
        display_text = linked_list.display()
        label.config(text=display_text, font=15)

    label = tk.Label(submenu)
    label.grid(row=7, column=1, padx=30, pady=30)

    pop_first_button = tk.Button(submenu, text="Eliminar el primer elemento",
                                 command=lambda: (linked_list.pop_first(), display_list()),
                                 bg='light blue', width=25, height=2, fg='blue')
    pop_button = tk.Button(submenu, text="Eliminar el último elemento",
                           command=lambda: (linked_list.pop(), display_list()),
                           bg='light blue', width=25, height=2, fg='blue')

    display_button = tk.Button(submenu, text="Mostrar Lista", command=lambda: (display_list()),
                               bg='light blue', width=25, height=2, fg='blue')

    prepend_button.grid(row=0, column=1, padx=20, pady=20)
    append_button.grid(row=1, column=1, padx=20, pady=20)
    pop_first_button.grid(row=2, column=1, padx=20, pady=20)
    pop_button.grid(row=3, column=1, padx=20, pady=20)
    search_button.grid(row=4, column=1, padx=20, pady=20)
    display_button.grid(row=5, column=1, padx=20, pady=20)


main_linked_list_button = tk.Button(window, text="Lista Enlazada", command=show_linked_list_menu, bg='light blue',
                                    width=40, height=5, font=('arial', 10))
main_linked_list_button.pack(pady=50)

# LISTA CIRCULAR

# Botón de prepend


def show_circular_list_menu():
    submenu = tk.Toplevel(window)
    submenu.title("Lista Circular")
    submenu.geometry("1100x700")

    prepend_button = tk.Button(submenu, text="Agregar elemento al inicio",
                               command=lambda: (add_to_front(), display_list()), bg='light blue',
                                    width=40, height=2, font=('arial', 10))
    append_button = tk.Button(submenu, text="Agregar elemento al final",
                              command=lambda: (add_to_end(), display_list()),
                              bg='light blue', width=40, height=2, font=('arial', 10))

    search_button = tk.Button(submenu, text="Buscar elemento",
                              command=lambda: (search_element(element_to_search)),
                              bg='light blue', width=40, height=2, font=('arial', 10))

    element_to_prepend = tk.Entry(submenu)
    element_to_prepend.grid(row=0, column=0, padx=50, pady=20)

    element_to_append = tk.Entry(submenu)
    element_to_append.grid(row=1, column=0, padx=50, pady=20)

    element_to_search = tk.Entry(submenu)
    element_to_search.grid(row=6, column=0, padx=50, pady=20)

    def add_to_front():
        data = element_to_prepend.get()
        circular_list.prepend(data)
        display_list()

    def add_to_end():
        data = element_to_append.get()
        circular_list.append(data)
        display_list()

    def search_element(entry):
        data = entry.get().strip()  # Obtener el valor del Entry sin espacios adicionales

        if not data:  # Verificar si está vacío
            messagebox.showwarning("Entrada vacía", "Por favor ingresa un valor para buscar.")
            return

        result = circular_list.search(data)  # Buscar por valor

        if result is not None:
            messagebox.showinfo("Búsqueda exitosa", f"Elemento '{data}' está en la lista.")
        else:
            messagebox.showinfo("Elemento no encontrado", f"Elemento '{data}' no está en la lista.")

    def display_list():
        display_text = circular_list.display()
        label.config(text=display_text)

    label = tk.Label(submenu, font=15)
    label.grid(row=4, column=6, padx=30, pady=30)

    pop_first_button = tk.Button(submenu, text="Eliminar el primer elemento",
                                 command=lambda: (circular_list.pop_first(), display_list()),
                                 bg='light blue', width=40, height=2, font=('arial', 10))
    pop_button = tk.Button(submenu, text="Eliminar el último elemento",
                           command=lambda: (circular_list.pop(), display_list()),
                           bg='light blue', width=40, height=2, font=('arial', 10))

    right_rotation_button = tk.Button(submenu, text="Rotar lista a la derecha",
                                      command=lambda: (circular_list.right_rotation(), display_list()),
                                      bg='light blue', width=40, height=2, font=('arial', 10))
    left_rotation_button = tk.Button(submenu, text="Rotar lista a la izquierda",
                                     command=lambda: (circular_list.left_rotation(), display_list()),
                                     bg='light blue', width=40, height=2, font=('arial', 10))

    display_button = tk.Button(submenu, text="Mostrar Lista", command=lambda: (display_list()),
                               bg='light blue', width=40, height=2, font=('arial', 10))

    prepend_button.grid(row=0, column=1, padx=20, pady=20)
    append_button.grid(row=1, column=1, padx=20, pady=20)
    pop_first_button.grid(row=2, column=1, padx=20, pady=20)
    pop_button.grid(row=3, column=1, padx=20, pady=20)
    right_rotation_button.grid(row=4, column=1, padx=20, pady=20)
    left_rotation_button.grid(row=5, column=1, padx=20, pady=20)
    search_button.grid(row=6, column=1, padx=20, pady=20)
    display_button.grid(row=7, column=1, padx=20, pady=20)


main_circular_list_button = tk.Button(window, text="Lista Circular", command=show_circular_list_menu, bg='light blue',
                                    width=40, height=5, font=('arial', 10))
main_circular_list_button.pack(pady=20)

window.mainloop()

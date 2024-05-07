import tkinter as tk
from main import linked_list  # Revisa si LinkedList está correctamente definido

# Ventana principal
window = tk.Tk()
window.geometry("500x500")
window.title("GESTIÓN DE LISTAS")

main_menu_frame = tk.Frame(window)
main_menu_frame.pack(padx=20, pady=20)

# Crear un `Frame` para el submenú
sub_menu_frame = tk.Frame(window)
sub_menu_frame.pack()  # Evitar mezcla de `pack()` y `grid()`

# Definición de `display_list`


def display_list():
    display_text = linked_list.display()  # Obtener la representación de la lista
    display_label.config(text=display_text)

# Entry para ingresar datos para `prepend`


element_to_prepend = tk.Entry(sub_menu_frame, width=20)
element_to_prepend.pack(pady=10)


window.mainloop()
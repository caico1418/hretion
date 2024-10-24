import tkinter as tk

def add_placeholder(entry, placeholder, isPassword=False):
    """ Agregar el placeholder al campo """
    entry.insert(0, placeholder)
    entry.config(fg='grey', font=("Arial", 12), justify="center")

    def on_focus_in(event):
        """ Eliminar el placeholder """
        print("Focus In:", entry.get())  # Depuración
        if entry.get() == placeholder:
            entry.delete(0, "end")  # Elimina el texto
            entry.config(fg="black")  # Cambia el color del texto

            # Valida si es un campo de contraseña
            if isPassword:
                entry.config(show="*")

    def on_focus_out(event):
        """ Agrega el placeholder si el campo está vacío """
        print("Focus Out:", entry.get())
        if entry.get() == "":
            entry.insert(0, placeholder)  # Restaura el placeholder
            entry.config(fg="grey")

            # Valida si es un campo de contraseña
            if isPassword:
                entry.config(show="")

    # Vincula los eventos de foco -> focus
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def only_letters(char):
    """ Verificar si el carácter es una letra """
    return char.isalpha() or char == ""
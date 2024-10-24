import tkinter as tk
from tkinter import messagebox

# Función que simula la validación del login
def validar_login():
    usuario = entry_user.get()
    contraseña = entry_pass.get()

    # Simulación de credenciales correctas (en la realidad se debe hacer una consulta a base de datos)
    if usuario == "admin" and contraseña == "1234":
        messagebox.showinfo('Éxito', 'Inicio de sesión exitoso')
        mostrar_sistema()  # Mostrar el frame del sistema
    else:
        messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

# Función para mostrar el frame del sistema (después de iniciar sesión)
def mostrar_sistema():
    frame_login.pack_forget()  # Ocultar el frame de login
    frame_sistema.pack(fill="both", expand=True)  # Mostrar el frame del sistema

# Función para cerrar sesión
def cerrar_sesion():
    frame_sistema.pack_forget()  # Ocultar el frame del sistema
    frame_login.pack(fill="both", expand=True)  # Mostrar el frame de login

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Login")
root.geometry("400x300")

# Frame de login
frame_login = tk.Frame(root)
frame_login.pack(fill="both", expand=True)

# Widgets del frame de login
label_user = tk.Label(frame_login, text="Usuario:")
label_user.pack(pady=10)
entry_user = tk.Entry(frame_login)
entry_user.pack(pady=10)

label_pass = tk.Label(frame_login, text="Contraseña:")
label_pass.pack(pady=10)
entry_pass = tk.Entry(frame_login, show="*")
entry_pass.pack(pady=10)

button_login = tk.Button(frame_login, text="Iniciar Sesión", command=validar_login)
button_login.pack(pady=20)

# Frame del sistema (se muestra al iniciar sesión)
frame_sistema = tk.Frame(root)

# Widgets del frame del sistema
label_bienvenida = tk.Label(frame_sistema, text="¡Bienvenido al sistema!", font=("Arial", 18))
label_bienvenida.pack(pady=50)

button_logout = tk.Button(frame_sistema, text="Cerrar Sesión", command=cerrar_sesion)
button_logout.pack(pady=20)

# Ejecutar la ventana
root.mainloop()


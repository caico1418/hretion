import tkinter as tk
from tkinter import ttk, messagebox
from components.placeholder import add_placeholder, only_letters
from services.register_user import registerUser
import re

class FrameFormRegister(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=650, style="RContent.TFrame")
        self.pack(side="left", fill="both", expand=False)
        self.propagate(False)

        # Titulo del registro
        name = ttk.Label(self, text="HRETION", font=("Arial", 40, "bold"), background="#FFFFFF")
        name.pack(pady=45, anchor="n")

        ## ejecuta la funcion
        self.formRegister()

    def formRegister(self):
        # crear frame para el formulario
        form_register = ttk.Frame(self, width=350, height=650, style='RContent.TFrame')
        form_register.pack(anchor='n', pady=(10, 0))
        form_register.propagate(False)


        ## Campo del nombre
        self.entry_full_name = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_full_name.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_full_name, "Full Name")

        ## Campo del nombre del hotel
        self.entry_hotel_name = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_hotel_name.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_hotel_name, "Name Hotel")

        ## Campo del numero de telefono
        self.entry_tel = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_tel.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_tel, "Phone Number")


        self.entry_tel.config(validate='key')
        self.entry_tel.bind("<KeyRelease>", lambda event: limit_length(self.entry_tel, 10))

        def limit_length(entry, max_length):
            """ Limitar la longitud del Entry a max_length. """
            if len(entry.get()) > max_length:
                entry.delete(max_length, tk.END)  # Eliminar caracteres que excedan el límite

        ## Campo del correo electronico
        self.entry_mail = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_mail.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_mail, "example@example.com")

        ## Campo de la password
        self.entry_password = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_password.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_password, "Password", True)

        ## Campo de la confirmacion de la password
        self.entry_password_confirm = tk.Entry(form_register, width=65, bg="#ECF0F1", font=("Arial", 14, "bold"), bd=0, justify="center")
        self.entry_password_confirm.pack(anchor="w", padx=(10, 0), pady=(0, 15), ipady=10)
        add_placeholder(self.entry_password_confirm, "Confirm Password", True)



        # valida si la contraseña tiene almenos un caracter especial
        def has_special_character(password):
            # Verificar si hay al menos un carácter especial en la contraseña
            return bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password))



        # funcion que envia los datos a la base de datos
        def registerUsuario(event=None):
            if any([
                self.entry_full_name.get() == "",
                self.entry_full_name.get() == "Full Name",
                self.entry_hotel_name.get() == "",
                self.entry_hotel_name.get() == "Name Hotel",
                self.entry_tel.get() == "",
                self.entry_tel.get() == "Phone Number",
                self.entry_mail.get() == "",
                self.entry_mail.get() == "example@example.com",
                self.entry_password.get() == "",
                self.entry_password.get() == "Password",
                self.entry_password_confirm.get() == "",
                self.entry_password_confirm.get() == "Confirm Password"
            ]):
                messagebox.showinfo('Advertencia', 'Llene los campos del formulario')
                return  # Salir de la función si hay campos vacíos

            # validate password
            password = self.entry_password.get()
            confirmPassword = self.entry_password_confirm.get()

            # Validar que la contraseña contenga al menos un carácter especial
            if not has_special_character(password):
                messagebox.showerror('Error', 'La contraseña debe contener al menos un carácter especial.')
                return  # Salir de la función si no hay caracteres especiales

            if password == confirmPassword:
                registerUser(self.entry_full_name.get(), self.entry_hotel_name.get(), self.entry_tel.get(), self.entry_mail.get(), password)
            else:
                messagebox.showerror('Error', 'Las contraseñas no son iguales')


        login_button = tk.Button(form_register, text="Create account", font=("Arial", 12, "bold"), bg="#2E4053",
                                 fg="white",
                                 activebackground="#5d6d7e", activeforeground="white", bd=0,
                                 highlightthickness=0,
                                 cursor="hand2", command=registerUsuario)
        login_button.focus()
        login_button.pack(anchor="center", padx=(10, 0), pady=(20, 10), ipadx=30, ipady=9)

        # Evento para el enter
        self.entry_full_name.bind('<Return>', registerUsuario)
        self.entry_hotel_name.bind('<Return>', registerUsuario)
        self.entry_tel.bind('<Return>', registerUsuario)
        self.entry_mail.bind('<Return>', registerUsuario)
        self.entry_password.bind('<Return>', registerUsuario)
        self.entry_password_confirm.bind('<Return>', registerUsuario)
        self.bind('<Return>', registerUsuario)



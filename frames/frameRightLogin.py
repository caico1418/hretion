import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from components.placeholder import add_placeholder
from services.login_services import validated_login

class FrameRightLogin(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=650, style="RContent.TFrame")
        self.pack(side='right', fill='both', expand=False)
        self.propagate(False)

        # titulo login
        name = ttk.Label(self, text="HRETION", font=("Arial", 40, "bold"), background="#FFFFFF")
        name.pack(pady=10, anchor="n")

        # imagen login
        self.imagen_logo = tk.PhotoImage(file="assets/logo_principal_200x200.png")
        label_image = tk.Label(self, image=self.imagen_logo, borderwidth=0)
        label_image.pack(anchor="center")


        # ejecutar login
        self.login()

    def login(self):
        form_login = ttk.Frame(self, width=250, height=325, style='RContent.TFrame')
        form_login.pack(anchor="center")
        form_login.propagate(False)


        # Label User
        label_username = ttk.Label(form_login, text="Username", font=("Arial", 15), background="#FFFFFF")
        label_username.pack(anchor="w", padx=(10, 5), pady=(10, 5))


        # Entry User
        self.entry_username = tk.Entry(form_login, width=30, bg='#ECF0F1', justify="center", font=("Arial", 10), bd=0)
        self.entry_username.pack(anchor="w", padx=(10, 0), pady=(0, 10), ipady=10)
        add_placeholder(self.entry_username, "username")

        # Label Password
        label_password = ttk.Label(form_login, text="Password", font=("Arial", 15), background="#FFFFFF")
        label_password.pack(anchor="w", padx=(10, 5), pady=(10, 5))


        # Entry Password
        self.entry_password = tk.Entry(form_login, width=30, bg='#ECF0F1', justify="center", font=("Arial", 10), bd=0)
        self.entry_password.pack(anchor="w", padx=(10, 0), pady=(0, 10), ipady=10)
        add_placeholder(self.entry_password, "password", True)

        # label forgot password
        forgot_password = ttk.Label(form_login, text="Forgot your password?",
                                    font=("Arial", 10, "bold", "underline"),
                                    background="#FFFFFF",
                                    foreground="#0076EB",
                                    cursor="hand2")
        forgot_password.pack(anchor="center", padx=(55, 0), pady=(5, 5), ipadx=30, ipady=7)




        def on_click(event=None):
            if any([
                self.entry_username.get() == "",
                self.entry_username.get() == "username",
                self.entry_password.get() == "",
                self.entry_password.get() == "password"
            ]):
                messagebox.showerror('Error', 'Los campos deben contener informacion')
                return
            # usuario y contraseña
            validated_login(self.entry_username.get(), self.entry_password.get())

        # boton
        login_button = tk.Button(form_login, text="Login", font=("Arial", 12, "bold"), bg="#2E4053", fg="white",
                                 activebackground="#5d6d7e", activeforeground="white", bd=0,
                                 highlightthickness=0,
                                 cursor="hand2", command=on_click)
        login_button.focus()
        login_button.pack(anchor="center", padx=(10, 0), pady=(20, 10), ipadx=30, ipady=7)

        self.entry_username.bind('<Return>', on_click)
        self.entry_password.bind('<Return>', on_click)
        # vincular la tecla enter a la ventana
        self.bind('<Return>', on_click)











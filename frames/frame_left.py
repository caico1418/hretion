import tkinter as tk
from tkinter import ttk
from components.rounded_button import RoundedButton



class FrameLeftImage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=350, height=650, style="RContent.TFrame")
        self.x_pos = 0  # Inicializa la posición del frame
        self.parent = parent  # Referencia al parent (App)
        self.frame_left = self  # Para que haga referencia a sí mismo
        self.login_button = None  # Para el botón de Login

        # Colocar el frame en la posición inicial con el tamaño deseado
        self.place(x=self.x_pos, y=0, width=500, height=650)
        self.propagate(False)

        # Cargar imagen de fondo
        self.imagen = tk.PhotoImage(file="assets/background-left-word.png")
        self.label_image = tk.Label(self, image=self.imagen, borderwidth=0)
        self.label_image.pack(anchor="w")

        # Segundo frame para el contenido
        self.content = ttk.Frame(self, padding=0, style='Content.TFrame')
        self.content.place(relx=0.5, rely=0.5, anchor="center")

        # Aplicar estilo al segundo frame
        style = ttk.Style()
        style.configure('Content.TFrame', background="#2E4053")

        # Label para "Don't have an account?"
        self.label_question = ttk.Label(self.content, text="Don't have an account?",
                                        font=("Arial", 13, "underline"),
                                        foreground="#FFFFFF", background="#2E4053", padding=(10, 5))
        self.label_question.pack(pady=(6, 10))

        # Añadir botón redondeado para "Sign up"
        self.signup_button = RoundedButton(self.content, text="Sign up", width=150, height=50, corner_radius=25,
                                           bg="#ffffff", cursor="hand2", command=lambda: self.mover_frame('derecha'))
        self.signup_button.pack(pady=(10, 0))

    def mover_frame(self, direccion):
        x_inicial = self.winfo_x()
        if direccion == 'derecha':
            x_final = self.parent.winfo_width() - self.winfo_width()  # Mueve a la derecha
        elif direccion == 'izquierda':
            x_final = 0  # Mueve a la izquierda
        else:
            return

        distancia_total = x_final - x_inicial
        tiempo_total = 1000  # Duración total de la animación en milisegundos
        fps = 60  # Fotogramas por segundo
        pasos_totales = int(fps * (tiempo_total / 1000))
        paso_actual = 0
        paso_size = distancia_total / pasos_totales  # Calcular el tamaño del paso

        def animar():
            nonlocal paso_actual
            if paso_actual <= pasos_totales:
                # Usar interpolación cuadrática
                t = paso_actual / pasos_totales
                t_suavizado = t ** 2 * (3 - 2 * t)  # Fórmula de suavizado (ease-in/ease-out)
                nuevo_x = x_inicial + distancia_total * t_suavizado

                self.place(x=nuevo_x, y=0)
                self.lift()
                paso_actual += 1
                self.after(int(1000 / fps), animar)  # Controlar la frecuencia de actualización
            else:
                # Asegurar que el frame termine en la posición final exacta
                self.place(x=x_final, y=0)
                if direccion == 'derecha':
                    self.animacion_final_derecha()
                elif direccion == 'izquierda':
                    self.animacion_final_izquierda()

        animar()

    def animacion_final_derecha(self):
        """Acciones después de mover el frame a la derecha."""
        self.label_question.pack_forget()
        self.signup_button.pack_forget()
        # Cambiar la imagen de fondo
        self.new_background_image = tk.PhotoImage(file="assets/welcome.png")
        self.label_image.config(image=self.new_background_image)
        self.mostrar_boton_login()

    def animacion_final_izquierda(self):
        """Acciones después de mover el frame a la izquierda."""
        self.label_image.config(image=self.imagen)
        self.label_question.pack(pady=(6, 10))
        self.signup_button.pack(pady=(10, 0))
        if self.login_button:
            self.login_button.destroy()
            self.login_button = None

    def mostrar_boton_login(self):
        """Mostrar botón de Login después de mover el frame."""
        if self.login_button is None:
            # Crear el botón de Login
            self.login_button = RoundedButton(self.content, text="Login", width=100, height=40,
                                              corner_radius=25, bg="#ffffff", cursor="hand2",
                                              command=lambda: self.mover_frame('izquierda'))
            self.login_button.pack(pady=(10, 0))







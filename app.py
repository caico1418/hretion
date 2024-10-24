import tkinter as tk
from tkinter import ttk
from components.rounded_button import RoundedButton
from styles.theme import set_theme
from frames.frame_left_register import FrameFormRegister
from frames.frame_left import FrameLeftImage
from frames.frameRightLogin import FrameRightLogin



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configuration()
        self.center_window()

        self.x_pos = 0
        self.frame_left = None
        self.login_button = None




        self.frame_left = FrameFormRegister(self)  # Frame izquierdo
        self.frame_left_image = FrameLeftImage(self) # Frame izquierdo con imagen
        self.frame_right_login = FrameRightLogin(self) # Frame derecho login




        # Llamar estilos
        set_theme(self)

    def configuration(self):
        self.title("HRETION")
        self.config(bg="white")

    def center_window(self):
        width, height = 1000, 650
        x = self.winfo_screenwidth() // 2 - width // 2
        y = self.winfo_screenheight() // 2 - height // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(False, False)





if __name__ == "__main__":
    app = App()
    app.mainloop()

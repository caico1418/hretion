from tkinter import ttk

def set_theme(app):
    style = ttk.Style(app)
    style.configure('RContent.TFrame', background='#FFFFFF')
    style.configure('Content.TFrame', background='#2E4053')
    style.configure('MContent.TFrame', background='#000000')

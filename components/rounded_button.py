import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, width=150, height=50, corner_radius=25, command=None, cursor="hand2", **kwargs):
        super().__init__(parent, width=width, height=height, bg=kwargs.get('bg', "#2E4053"), highlightthickness=0, cursor=cursor)

        self.command = command
        self.round_rect = self.create_rounded_rectangle(0, 0, width, height, corner_radius, fill=kwargs.get('bg', "#3498DB"))
        self.text = self.create_text(width // 2, height // 2, text=text, fill="black", font=("Arial", 12, "bold"))
        self.bind("<Button-1>", self.on_click)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1 + radius,
                  x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2 - radius, y2, x2 - radius, y2,
                  x1 + radius, y2, x1 + radius, y2, x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_click(self, event):
        if self.command:
            self.command()

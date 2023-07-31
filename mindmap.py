import tkinter as tk
from tkinter import ttk

class MindMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Map Application")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.shapes = []
        self.current_shape = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def create_shape(self, shape_type, x, y):
        if shape_type == "rectangle":
            return self.canvas.create_rectangle(x, y, x + 100, y + 50, fill="lightblue", outline="black")
        elif shape_type == "oval":
            return self.canvas.create_oval(x, y, x + 80, y + 80, fill="lightgreen", outline="black")
        elif shape_type == "text":
            return self.canvas.create_text(x, y, text="Text Box", font=("Arial", 12), anchor=tk.NW)
        else:
            return None

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        shape_type = "rectangle"  # Change this to select different shapes
        self.current_shape = self.create_shape(shape_type, self.start_x, self.start_y)

    def on_drag(self, event):
        if self.current_shape:
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        if self.current_shape:
            self.shapes.append(self.current_shape)
            self.current_shape = None

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMapApp(root)
    root.mainloop()

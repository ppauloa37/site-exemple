import tkinter as tk
from tkinter import colorchooser

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=brush_size)
    last_x, last_y = event.x, event.y

def choose_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def use_eraser():
    global color
    color = "white"

def set_brush_size(new_size):
    global brush_size
    brush_size = new_size

root = tk.Tk()
root.title("Paint App Pinte")

color = "black"
brush_size = 5

canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", draw)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Cor", command=choose_color).pack(side=tk.LEFT)
tk.Button(frame, text="Borracha", command=use_eraser).pack(side=tk.LEFT)

size_slider = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Tamanho")
size_slider.set(brush_size)
size_slider.pack(side=tk.LEFT)
size_slider.config(command=lambda val: set_brush_size(int(val)))

root.mainloop()
import tkinter as tk
from tkinter import colorchooser

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=brush_size)
    last_x, last_y = event.x, event.y

def choose_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def use_eraser():
    global color
    color = "white"

def set_brush_size(new_size):
    global brush_size
    brush_size = new_size

root = tk.Tk()
root.title("Simple Paint App")

color = "black"
brush_size = 5

canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", draw)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Cor", command=choose_color).pack(side=tk.LEFT)
tk.Button(frame, text="Borracha", command=use_eraser).pack(side=tk.LEFT)

size_slider = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Tamanho")
size_slider.set(brush_size)
size_slider.pack(side=tk.LEFT)
size_slider.config(command=lambda val: set_brush_size(int(val)))

root.mainloop()

import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Calculator")

# Allow constants and functions from math library
allowed_values = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
allowed_values.update({'pi': math.pi, 'e': math.e, 'sqrt': math.sqrt})


    

root.mainloop()
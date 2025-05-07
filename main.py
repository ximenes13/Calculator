import tkinter as tk
import math

# Allow constants and functions from math library
allowed_values = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
allowed_values.update({'pi': math.pi, 'e': math.e, 'sqrt': math.sqrt})


def evaluate_math(expr):
    try:
        return eval(expr, {"__builtins__": {}}, allowed_values)
    except Exception:
        return "Error"


def on_click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        expr = entry.get()
        result = evaluate_math(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create main window
root = tk.Tk()
root.title("Calculator")

# Create entry
entry = tk.Entry(root, width=40, font=("Helvetica", 20), borderwidth=3, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Fixed columnspan to 4 to match layout

# Buttons Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('pi', 5, 2), ('C', 5, 3)
]

# Create Buttons
for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear
    else:
        cmd = lambda t=text: on_click(t)

    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the app
root.mainloop()

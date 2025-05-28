import tkinter as tk
import math

# Allow constants and functions from math library
allowed_values = {
    k: v for k, v in math.__dict__.items() if not k.startswith("_")
}
# Use degrees for trigonometric functions
allowed_values.update({
    'pi': math.pi,
    'e': math.e,
    'sqrt': math.sqrt,
    'sin': lambda x: math.sin(math.radians(x)),
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
})

# Themes
themes = {
            "light": {
                "bg": "#ffffff",
                "fg": "#000000",
                "entry_bg": "#ffffff",
                "entry_fg": "#000000",
                "button_bg": "#e0e0e0",
                "button_fg": "#000000"
            },
            "dark": {
                "bg": "#2e2e2e",
                "fg": "#ffffff",
                "entry_bg": "#3c3f41",
                "entry_fg": "#ffffff",
                "button_bg": "#444444",
                "button_fg": "#ffffff"
            }
        }

current_theme = "light"
buttons_list = []

def evaluate_math(expr):
    try:
        return eval(expr, {"__builtins__": {}}, allowed_values)
    except Exception:
        return "Error"


def on_click(value):
    operators = ["+", "-", "*", "/", ".", "(", ")"]
    functions = ["pi", "sqrt", "sin", "cos", "tan"]
    current = entry.get()

    if current == "Error":
        entry.delete(0, tk.END)
        current = ""

    # Prevent duplicate consecutive functions
    if current:
        last_token = current.split()[-1]  # Split expression (for more complex logic)
        if current[-1].isalpha() and value in functions:
            return  # Don't allow stacking functions like "sinsqrt"

        if current[-1] in operators and value in operators:
            # Replace last operator with the new one
            entry.delete(len(current) - 1, tk.END)
            entry.insert(tk.END, value)
            return

    # Prevent two functions in a row (by checking the last word)
    for func in functions:
        if current.endswith(func) and value in functions:
            return  # Skip inserting another function

    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)


def calculate():
    expr = entry.get()
    result = evaluate_math(expr)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = themes[theme_name]
    root.configure(bg=theme["bg"])
    entry.configure(bg=theme["entry_bg"], # background color
                    fg=theme["entry_fg"], # text color
                    insertbackground=theme["entry_fg"]) # cursor color
    for btn in buttons_list:
        btn.configured(
        bg = theme["button_bg"],
        fg = theme["button_fg"],
        activebackground=theme["button_bg"], # color when pressed
        activeforeground=theme["button_fg"] # color when pressed
        )
    dark_btn.configure(bg=theme["button_bg"], fg="#ffffff")
    light_btn.configure(bg=theme["button_bg"], fg="#ffffff")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("510x440")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, width=40, font=("Helvetica", 20), borderwidth=3, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('pi', 5, 2), ('C', 5, 3),
    ('sqrt', 6, 0), ('sin', 6, 1), ('cos', 6, 2), ('tan', 6, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear
    else:
        cmd = lambda t=text: on_click(t)

    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Theme switch buttons
dark_btn = tk.Button(root, text="🌙", command=lambda: apply_theme("dark"))
dark_btn.grid(row=7, column=0, columnspan=2, sticky="we", padx=10, pady=10)

light_btn = tk.Button(root, text="☀️", command=lambda: apply_theme("light"))
light_btn.grid(row=7, column=2, columnspan=2, sticky="we", padx=10, pady=10)

apply_theme("light")  # Apply initial theme

root.mainloop()

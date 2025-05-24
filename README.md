# 🧮 Calculator App with Python + Tkinter

This project is a desktop calculator built using Python and Tkinter, designed to perform basic and scientific arithmetic operations through a graphical user interface. Users can input expressions involving addition, subtraction, multiplication, division, parentheses, π, sen(), cos(), tan() and sqrt() — with real-time evaluation and a clean reset function.

---

## 🚀 Features
🧠 Supports fundamental arithmetic operations: +, -, ×, ÷ <br>
🧮 Handles complex expressions using parentheses () <br>
🧷 Built-in support for π (pi) using Python's math module <br>
🔁 Clear (C) button to reset the display instantly <br>
🎯 Equals (=) button to evaluate full expressions <br>
🪟 Clean and intuitive interface using Tkinter widgets <br>
🛠️ Designed for extensibility — easily add new functions or features <br>
🔬 Scientific functions support:
  - sqrt(x): Calculates the square root of x
  - tan(x): Calculates the tangent of the angle x (in radians)
  - cos(x): Calculates the cosine of the angle x (in radians)
  - sen(x): Calculates the sine of the angle x (in radians)

---

## 🖥️ Technologies Used

- Python 3.x
- Tkinter (for GUI interface)
- Math module (for π constant and scientific functions like sqrt, tan, cos, and sen)
- PyCharm (recommended IDE)

---

## 📂 Project Structure

- **main.py**: This is the core script of the calculator app. It contains both the user interface and logic for evaluating mathematical expressions. Key responsibilities:
  - 🖼️ Builds the GUI using Tkinter (entry field and button grid layout) <br>
  - 🧠 Safely evaluates math expressions using Python’s eval() with a restricted scope <br>
  - ➕ Supports operations: +, -, *, /, (), pi, and decimal points <br>
  - 🔁 Implements functional buttons: =, C (clear), and numeric input <br>
  - 🧰 Uses the math module for constants like pi and functions like sqrt, tan, cos, and sen <br>
  - ❌ Handles invalid input gracefully by displaying Error

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/Calculator.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the calculator app.

`python3 main.py`

---

# 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Calculator/issues).

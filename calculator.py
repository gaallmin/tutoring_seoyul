import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Calculator with Graphing")

        # 입력칸
        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, insertwidth=2, width=18, borderwidth=4)
        input_field.grid(row=0, column=0, columnspan=4)

        # 버튼 칸
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/', 'x', 
            '4', '5', '6', '*', 'DEL', 
            '1', '2', '3', '-', '^', 
            '0', '.', '=', '+', 'C'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(button_frame, text=button, width=10, height=3, font=('Arial', 18), bd=1, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

        tk.Button(self.root, text="Draw Graph", width=15, height=2, font=('Arial', 14), command=self.draw_graph).pack()

    def on_button_click(self, button):
        if button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        elif button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == "DEL":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

    def draw_graph(self):
        expression = self.expression

        if 'x' in expression and '^' in expression:
            try:
                x = np.linspace(-10, 10, 400)
                y = eval(expression.replace('^', '**').replace('x', 'x'))
                plt.figure(figsize=(6, 4))
                plt.plot(x, y, label=f'y = {expression}')
                plt.title('Graph')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.legend()
                plt.grid(True)
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", "Unable to plot graph. Ensure the expression is a valid function of x.")
        else:
            messagebox.showwarning("Input Needed", "Enter an expression to draw a graph.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


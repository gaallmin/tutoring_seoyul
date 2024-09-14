import tkinter as tk
from tkinter import messagebox

def machine(coin, button):
    if coin == 500:
        if button == '파인':
            return '파인'
        elif button == '복숭아':
            return '복숭아'
        else:
            return '자두'
    else:
        return None

def on_submit():
    try:
        coin = int(coin_entry.get())
        button = button_entry.get()
        result = machine(coin, button)
        if result:
            result_label.config(text=f"Output: {result}")
        else:
            messagebox.showerror("Error", "Invalid coin or button")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the coin")

window = tk.Tk()
window.title("Machine GUI")

coin_label = tk.Label(window, text="Enter coin:")
coin_label.pack()

coin_entry = tk.Entry(window)
coin_entry.pack()

button_label = tk.Label(window, text="Enter button:")
button_label.pack()

button_entry = tk.Entry(window)
button_entry.pack()


submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(window, text="Output: ")
result_label.pack()

window.mainloop()

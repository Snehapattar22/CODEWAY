import tkinter as tk

window = tk.Tk()
window.title("Python Calculator")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    global first_number
    first_number = float(entry.get())
    global operation
    operation = "add"
    entry.delete(0, tk.END)

def button_equal():
    second_number = float(entry.get())
    if operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    elif operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        if second_number == 0:
            result = "Error: Division by zero"
        else:
            result = first_number / second_number
    else:
        result = "Invalid operation"
    entry.delete(0, tk.END)
    entry.insert(0, result)

def button_subtract():
    global first_number
    first_number = float(entry.get())
    global operation
    operation = "subtract"
    entry.delete(0, tk.END)

def button_multiply():
    global first_number
    first_number = float(entry.get())
    global operation
    operation = "multiply"
    entry.delete(0, tk.END)

def button_divide():
    global first_number
    first_number = float(entry.get())
    global operation
    operation = "divide"
    entry.delete(0, tk.END)

entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_0 = tk.Button(window, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=1)
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=0)
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=1)
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=2)
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=0)
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=1)
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=2)

button_divide = tk.Button(window, text="/", command=button_divide)
button_divide.grid(row=2, column=3)
button_multiply = tk.Button(window, text="*", command=button_multiply)
button_multiply.grid(row=3, column=3)
button_subtract = tk.Button(window, text="-", command=button_subtract)
button_subtract.grid(row=4, column=1)
button_add = tk.Button(window, text="+", command=button_add)
button_add.grid(row=4, column=2)
button_equal = tk.Button(window, text="=", command=button_equal)
button_equal.grid(row=4, column=3)
button_clear = tk.Button(window, text="C", command=button_clear)
button_clear.grid(row=1, column=3)

window.mainloop()

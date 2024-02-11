import tkinter as tk
import random
import string

def generate_password():
  """
  Generates a random password based on user-selected criteria.
  """
  length_text = length_entry.get()
  if not length_text:
    popup_error_message("Please enter a desired password length.")
    return
  else:
    try:
      length = int(length_text)
    except ValueError:
      popup_error_message("Invalid length input. Please enter a number.")
      return

  lowercase_selected = lowercase_var.get()
  uppercase_selected = uppercase_var.get()
  numbers_selected = numbers_var.get()
  symbols_selected = symbols_var.get()

  characters = ""
  if lowercase_selected:
    characters += string.ascii_lowercase
  if uppercase_selected:
    characters += string.ascii_uppercase
  if numbers_selected:
    characters += string.digits
  if symbols_selected:
    characters += "!@#$%^&*()"

  if not characters:
    popup_error_message()
    return

  password = "".join(random.choice(characters) for _ in range(length))
  password_label["text"] = password

def popup_error_message(message="Please choose at least one character type."):
  
  popup = tk.Toplevel()
  popup.title("Error")
  popup_message = tk.Label(popup, text=message)
  popup_message.pack()
  popup.mainloop()

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

lowercase_var = tk.IntVar(value=1)  
lowercase_checkbox = tk.Checkbutton(root, text="lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=0)

uppercase_var = tk.IntVar(value=1)  
uppercase_checkbox = tk.Checkbutton(root, text="uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=2, column=0)

numbers_var = tk.IntVar(value=1)  
numbers_checkbox = tk.Checkbutton(root, text="numbers", variable=numbers_var)
numbers_checkbox.grid(row=3, column=0)

symbols_var = tk.IntVar(value=1)  
symbols_checkbox = tk.Checkbutton(root, text="symbols", variable=symbols_var)
symbols_checkbox.grid(row=4, column=0)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

password_label = tk.Label(root, text="...")
password_label.grid(row=6, column=0, columnspan=2)

root.mainloop()

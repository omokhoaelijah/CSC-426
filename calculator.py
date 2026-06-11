import tkinter as tk

def button_click(item):
    """Handles button clicks and updates the display."""
    current = display_var.get()
    
    # Handle the integer division symbol translation for Python
    if item == '\\':
        item = '//'
    # Handle the exponent symbol translation for Python
    elif item == '^':
        item = '**'
        
    display_var.set(current + str(item))

def button_clear():
    """Clears the display."""
    display_var.set("")

def button_equal():
    """Evaluates the mathematical expression in the display."""
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Error: Div by Zero")
    except Exception:
        display_var.set("Error")

# --- GUI Setup ---
root = tk.Tk()
root.title("CSC426 Calculator")
root.geometry("320x420")
root.resizable(0, 0)
root.configure(bg="#f0f0f0")

# --- Display Screen ---
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24, 'bold'), 
                   bg="#e8e8e8", fg="black", bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

# --- Button Layout ---
# We define the buttons exactly as requested in the assignment parameters
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('\\', 5, 0), ('^', 5, 1), ('%', 5, 2)
]

# --- Create and Place Buttons ---
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#4caf50", fg="white",
                        command=button_equal, height=2, width=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#f44336", fg="white",
                        command=button_clear, height=2, width=5)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg="#ffffff",
                        command=lambda t=text: button_click(t), height=2, width=5)
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
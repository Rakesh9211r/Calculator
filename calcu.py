import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display screen
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Create the buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for button in row:
        b = tk.Button(frame, text=button, font="lucida 15 bold", relief=tk.RAISED, bd=3)
        b.pack(side=tk.LEFT, expand=True, fill="both")
        b.bind("<Button-1>", on_click)

# Start the application
root.mainloop()
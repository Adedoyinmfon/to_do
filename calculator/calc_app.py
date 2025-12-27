import tkinter as tk

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=20, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        tk.Button(root, text=btn, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=btn, width=5, height=2,
                  command=lambda b=btn: press(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=22, command=clear)\
    .grid(row=row, column=0, columnspan=4)

root.mainloop()
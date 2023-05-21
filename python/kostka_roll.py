import tkinter as tk
import random as rand

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = rand.randint(1, 6)

window = tk.Tk()

window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="Roll", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=1, column=0)

window.mainloop()

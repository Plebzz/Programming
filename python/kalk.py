import tkinter as tk
import math

window = tk.Tk()
window.title("Kalkulator")

field_text=""

def add_sth(sth):
    global field_text
    field_text=field_text+str(sth)
    lbl.delete("1.0", "end")
    lbl.insert("1.0", field_text)

def calc():
    global field_text
    result=str(eval(field_text))
    lbl.delete("1.0", "end")
    lbl.insert("1.0", result)

def ce():
    global field_text
    field_text=""
    lbl.delete("1.0", "end")

def perce():
    global field_text
    percent=float(field_text)/100
    lbl.delete("1.0", "end")
    lbl.insert("1.0", percent)

lbl = tk.Text(master=window, font=5, height=2, width=20)
frm_calc = tk.Frame(master=window)

btn_c = tk.Button(master=frm_calc, text="C", width=4, font=5, command=lambda: ce())
btn_perc = tk.Button(master=frm_calc, text="%", width=4, font=5, command=lambda: perce())
btn_div = tk.Button(master=frm_calc, text="/", width=4, font=5, command=lambda: add_sth("/"))
btn_empty = tk.Button(master=frm_calc, width=4, font=5)
btn_seven = tk.Button(master=frm_calc, text="7", width=4, font=5, command=lambda: add_sth(7))
btn_eight = tk.Button(master=frm_calc, text="8", width=4, font=5, command=lambda: add_sth(8))
btn_nine = tk.Button(master=frm_calc, text="9", width=4, font=5, command=lambda: add_sth(9))
btn_multi = tk.Button(master=frm_calc, text="X", width=4, font=5, command=lambda: add_sth("*"))
btn_four = tk.Button(master=frm_calc, text="4", width=4, font=5, command=lambda: add_sth(4))
btn_five = tk.Button(master=frm_calc, text="5", width=4, font=5, command=lambda: add_sth(5))
btn_six = tk.Button(master=frm_calc, text="6", width=4, font=5, command=lambda: add_sth(6))
btn_minus = tk.Button(master=frm_calc, text="-", width=4, font=5, command=lambda: add_sth("-"))
btn_one = tk.Button(master=frm_calc, text="1", width=4, font=5, command=lambda: add_sth(1))
btn_two = tk.Button(master=frm_calc, text="2", width=4, font=5, command=lambda: add_sth(2))
btn_three = tk.Button(master=frm_calc, text="3", width=4, font=5, command=lambda: add_sth(3))
btn_plus = tk.Button(master=frm_calc, text="+", width=4, font=5, command=lambda: add_sth("+"))
btn_zero = tk.Button(master=frm_calc, text="0", width=4, font=5, command=lambda: add_sth(0))
btn_dot = tk.Button(master=frm_calc, text=".", width=4, font=5, command=lambda: add_sth("."))
btn_equal = tk.Button(master=frm_calc, text="=", width=4, font=5, command=lambda: calc())
btn_empty2 = tk.Button(master=frm_calc, width=4, font=5)

lbl.grid(column=0, row=0, sticky="e")
frm_calc.grid(column=0, row=1)

btn_c.grid(column=0, row=0, sticky="nsew")
btn_perc.grid(column=1, row=0, sticky="nsew")
btn_div.grid(column=2, row=0, sticky="nsew")
btn_empty.grid(column=3, row=0, sticky="nsew")
btn_seven.grid(column=0, row=1, sticky="nsew")
btn_eight.grid(column=1, row=1, sticky="nsew")
btn_nine.grid(column=2, row=1, sticky="nsew")
btn_multi.grid(column=3, row=1, sticky="nsew")
btn_four.grid(column=0, row=2, sticky="nsew")
btn_five.grid(column=1, row=2, sticky="nsew")
btn_six.grid(column=2, row=2, sticky="nsew")
btn_minus.grid(column=3, row=2, sticky="nsew")
btn_one.grid(column=0, row=3, sticky="nsew")
btn_two.grid(column=1, row=3, sticky="nsew")
btn_three.grid(column=2, row=3, sticky="nsew")
btn_plus.grid(column=3, row=3, sticky="nsew")
btn_zero.grid(column=0, row=4, sticky="nsew")
btn_dot.grid(column=1, row=4, sticky="nsew")
btn_equal.grid(column=2, row=4, sticky="nsew")
btn_empty2.grid(column=3, row=4, sticky="nsew")

window.mainloop()
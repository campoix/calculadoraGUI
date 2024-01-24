import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("by: camps")
root.geometry("400x500")
root.resizable(False, False)


lbl1 = tk.Label(root, text="CLCLT!", font="Verdana 27 bold")
lbl1.pack()

lbl2 = tk.Label(root)
lbl2.place(anchor="nw", relx=0.5, rely=0.5) 

def raiz():
    print("raiz")
    
def adicao():
    print("mais")
    var1 = entry1_var1.get()
    var2 = entry2_var1.get()
    soma1 = var1 + var2
    lbl2.configure(text=soma1, font="Verdana 15")

def subtracao():
    var1 = entry1_var1.get()
    var2 = entry2_var1.get()
    sub1 = var1 - var2
    lbl2.configure(text=sub1, font="Verdana 15")

def multi():
    print("vezes")
    var1 = entry1_var1.get()
    var2 = entry2_var1.get()
    multi1 = var1 * var2
    lbl2.configure(text=multi1, font="Verdana 15")
def div():
    print("divisao")
    var1 = entry1_var1.get()
    var2 = entry2_var1.get()
    div1 = var1 / var2
    lbl2.configure(text=div1, font="Verdana 15")
def aocubo():
    print("ao cbo")

def aoquadrado():
    print("ao quadrado")



entry1_var1 = tk.DoubleVar()
entry1 = tk.Entry(root, width=6,font="Verdana 16",textvariable=entry1_var1)
entry1.place(anchor="nw", relx=0.15, rely=0.35)

entry2_var1 = tk.DoubleVar()
entry2 = tk.Entry(root, width=6,font="Verdana 16",textvariable=entry2_var1)
entry2.place(anchor="nw", relx=0.15, rely=0.45)

btn1 = tk.Button(root, text="+", font="Verdana 13 bold", background="gray93", height=1, width=4, command=adicao)
btn1.place(anchor="nw", relx=0.05, rely=0.61)

btn2 = tk.Button(root, text="-", font="Verdana 13 bold", background="gray93", height=1, width=4, command=subtracao)
btn2.place(anchor="nw", relx=0.25, rely=0.61)

btn3 = tk.Button(root, text="x", font="Verdana 13 bold", background="gray93", height=1, width=4, command=multi)
btn3.place(anchor="nw", relx=0.45, rely=0.61)

btn4 = tk.Button(root, text="÷", font="Verdana 13 bold", background="gray93", height=1, width=4, command=div)
btn4.place(anchor="nw", relx=0.65, rely=0.61)

root.mainloop()
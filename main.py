from tkinter import Tk, Entry, Text, Frame, NONE, mainloop
from func import *

calc = Tk()
calc.title("Calculadora")
calc.resizable(False, False)
calc.configure(bg='black')
calc.bind("<Key>", lambda event: on_key_press(event, display))


display = Text(calc, font="Arial 20 bold", bg="white", fg="black", height=3, width=19, wrap=NONE, bd=0) # Mudança de Entry para Text para poder usar o wrap=NONE. 
display.pack(fill='x', expand=True) # Mudança de grid para pack para poder usar o fill='x' e expand=True e assim o display ocupar toda a largura de sua linha.

painel = Frame(calc, bg="black")

# Botões

# row 0
create_button(painel, "(", lambda: insertValue(display, "("), 0, 0, bg="darkorange", fg="white")
create_button(painel, ")", lambda: insertValue(display, ")"), 0, 1, bg="darkorange", fg="white")
create_button(painel, "^", lambda: insertValue(display, "**"), 0, 2, bg="darkorange", fg="white")
create_button(painel, "√", lambda: insertValue(display, "sqrt("), 0, 3, bg="darkorange", fg="white")

# 1
create_button(painel, "7", lambda: insertValue(display, "7"), 1, 0, bg="#232323", fg="white")
create_button(painel, "8", lambda: insertValue(display, "8"), 1, 1, bg="#232323", fg="white")
create_button(painel, "9", lambda: insertValue(display, "9"), 1, 2, bg="#232323", fg="white")
create_button(painel, "/", lambda: insertValue(display, "/"), 1, 3, bg="darkorange", fg="white")

# row 2
create_button(painel, "4", lambda: insertValue(display, "4"), 2, 0, bg="#232323", fg="white")
create_button(painel, "5", lambda: insertValue(display, "5"), 2, 1, bg="#232323", fg="white")
create_button(painel, "6", lambda: insertValue(display, "6"), 2, 2, bg="#232323", fg="white")
create_button(painel, "*", lambda: insertValue(display, "*"), 2, 3, bg="darkorange", fg="white")

# row 3
create_button(painel, "1", lambda: insertValue(display, "1"), 3, 0, bg="#232323", fg="white")
create_button(painel, "2", lambda: insertValue(display, "2"), 3, 1 , bg="#232323", fg="white")
create_button(painel, "3", lambda: insertValue(display, "3"), 3, 2, bg="#232323", fg="white")
create_button(painel, "+", lambda: insertValue(display, "+"), 3, 3, bg="darkorange", fg="white")

# row 4
create_button(painel, "0", lambda: insertValue(display, "0"), 4, 0 , bg="#232323", fg="white")
create_button(painel, "=", lambda: calculate(display), 4, 1, bg="#232323", fg="white")
create_button(painel, "C", lambda: clear(display), 4, 2, bg="#232323", fg="white")
create_button(painel, "-", lambda: insertValue(display, "-"), 4, 3, bg="darkorange", fg="white")


painel.pack()

mainloop()

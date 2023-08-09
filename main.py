from tkinter import *

# Calculadora

calc = Tk()
calc.title("Calculadora")

# Actions
def insertValue(value):
    display.insert(END, value)

def clear():
    display.delete(0, END)

def calculate():
    result = eval(display.get())
    display.delete(0, END)
    display.insert(0, str(result))

display = Entry(calc, font="Arial 20 bold", bg="white", fg="black", width=19)
display.pack()

painel = Frame(calc, bg="black")

# Botões
# Primeira linha
btn7 = Button(painel, bg="white", fg="black", bd=1, text="7", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("7")).grid(row=0, column=0)
btn8 = Button(painel, bg="white", fg="black", bd=1, text="8", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("8")).grid(row=0, column=1)
btn8 = Button(painel, bg="white", fg="black", bd=1, text="9", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("9")).grid(row=0, column=2)
btnDiv = Button(painel, bg="white", fg="black", bd=1, text="/", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("/")).grid(row=0, column=3)

# Segunda linha
btn4 = Button(painel, bg="white", fg="black", bd=1, text="4", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("4")).grid(row=1, column=0)
btn5 = Button(painel, bg="white", fg="black", bd=1, text="5", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("5")).grid(row=1, column=1)
btn6 = Button(painel, bg="white", fg="black", bd=1, text="6", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("6")).grid(row=1, column=2)
btnMult = Button(painel, bg="white", fg="black", bd=1, text="*", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("*")).grid(row=1, column=3)

# Terceira linha
btn1 = Button(painel, bg="white", fg="black", bd=1, text="1", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("1")).grid(row=2, column=0)
btn2 = Button(painel, bg="white", fg="black", bd=1, text="2", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("2")).grid(row=2, column=1)
btn3 = Button(painel, bg="white", fg="black", bd=1, text="3", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("3")).grid(row=2, column=2)
btnSum = Button(painel, bg="white", fg="black", bd=1, text="+", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("+")).grid(row=2, column=3)

# Quarta linha
btn0 = Button(painel, bg="white", fg="black", bd=1, text="0", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("0")).grid(row=3, column=0)
btnEqual = Button(painel, bg="white", fg="black", bd=1, text="=", font="Arial 16 bold", width=5, height=3, command=calculate).grid(row=3, column=1)
btnClear = Button(painel, bg="white", fg="black", bd=1, text="C", font="Arial 16 bold", width=5, height=3, command=clear).grid(row=3, column=2)
btnSub = Button(painel, bg="white", fg="black", bd=1, text="-", font="Arial 16 bold", width=5, height=3, command=lambda: insertValue("-")).grid(row=3, column=3)


painel.pack()

mainloop()

from tkinter import Tk

# Programa que detecta teclas pressionadas no teclado e imprime no terminal.
# Usado para descobrir o nome das teclas para usar no programa principal.

def on_key_press(event):
    print("Tecla pressionada:", event.keysym)

root = Tk()
root.title("Detectar Tecla")
root.geometry("300x200")

root.bind("<KeyPress>", on_key_press)

root.mainloop()

# Teclas pressionadas:
# "Return", "KP_Enter", "equal"
# "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9"
# "BackSpace", "Delete"

from tkinter import Button, END

# Actions
def insertValue(display, value):
    display.insert(END, value)
    display.see(END)

def clear(display):
    display.delete("1.0", END)

def calculate(display):
    result = eval(display.get("1.0", END).strip())
    display.delete("1.0", END)
    display.insert(END, str(result))

def create_button(painel, text, command, row, col, bg="white", fg="black", bd=1, font="Arial 16 bold", width=5, height=3):
    return Button(painel, bg=bg, fg=fg, bd=bd, text=text, font=font, width=width, height=height, command=command).grid(row=row, column=col)

from tkinter import END

def on_key_press(event, display):
    if event.keysym in ["Return", "KP_Enter", "equal"]: # KP_Enter é o enter do teclado numérico (NumLock)e Return é o enter do teclado normal.
        calculate(display)
    elif event.keysym in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9"]:
        num = event.keysym if len(event.keysym) == 1 else event.keysym[-1] # Isso é para pegar o número do teclado numérico (NumLock) ignorando o "KP_".
        insertValue(display, num)
    elif event.keysym == "plus" or event.keysym == "KP_Add":
        insertValue(display, "+")
    elif event.keysym == "minus" or event.keysym == "KP_Subtract":
        insertValue(display, "-")
    elif event.keysym == "asterisk" or event.keysym == "KP_Multiply":
        insertValue(display, "*")
    elif event.keysym == "slash" or event.keysym == "KP_Divide":
        insertValue(display, "/")
    elif event.keysym == "parenleft":
        insertValue(display, "(")
    elif event.keysym == "parenright":
        insertValue(display, ")")
    elif event.keysym == "BackSpace" or event.keysym == "Delete":
        clear(display)

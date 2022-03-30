from tkinter import *
from tkinter.ttk import Combobox


def clickbtn():
    lbl.config(text=ent.get())


win = Tk()
win.title('Led')
win.geometry('300x350')

lbl = Label(win, text='bebra', font=("Impact", 50))
btn = Button(win, text='zanuhat', font=("Impact", 15), command=clickbtn)
ent = Entry(win, width=5, font=("Impact", 8))
cum = Combobox(win, font=("Impact", 8))
cum["values"] = 2, 5, 8, 10

lbl.pack(side=TOP)
btn.pack(side=TOP)
ent.pack(side=TOP)
cum.pack(side=TOP)

win.mainloop()

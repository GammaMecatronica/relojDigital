from cProfile import label
from tkinter import *
import time


reloj = Tk()
reloj.title("Reloj Digital")
reloj.geometry("420x150")
reloj.resizable(0,0)


label=Label(reloj,
font=('Yu Gothic UI',68,'bold'),
bg="cadet blue",fg='#e8e8e3',bd=40)
label.grid(row=0,column=1)

def reloj_digital():
    tiempo=time.strftime('%H:%M:%S')
    label.config(text=tiempo)
    label.after(200, reloj_digital)

reloj_digital()



reloj.mainloop()

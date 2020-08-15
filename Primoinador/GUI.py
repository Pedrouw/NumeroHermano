from tkinter import *
from tkinter import scrolledtext

ventana = Tk()
ventana.title("Primoinador")
ventana.geometry('600x350')

prs = Label(ventana, text=" ")
prs.grid(column=0, row=0)

texto_sup = Label(ventana, text="El Primoinador!", font=("Consolas", 15))
texto_sup.grid(column=4, row=1)

texto_inf = Label(ventana, text="El ''-inador'' para encontrar números primos", font=("Consolas", 10))
texto_inf.grid(column=4, row=2)

dsd = Label(ventana, text="Desde el: ", font=("Consolas", 9))
dsd.grid(column=2, row=5)

num1_inpt = Entry(ventana, width=10)
num1_inpt.grid(column=3, row=5)

hst = Label(ventana, text=" hasta el: ", font=("Consolas", 9))
hst.grid(column=4, row=5)

num2_inpt = Entry(ventana, width=10)
num2_inpt.grid(column=5, row=5)

act_btn = Button(ventana, text="Encontrar primos")
act_btn.grid(column=4, row=7)

rslt = scrolledtext.ScrolledText(ventana, width=40, height=10)
rslt.grid(column= 4, row=9)
rslt.config(state=DISABLED)

ventana.mainloop()
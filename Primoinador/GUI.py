from tkinter import *
from tkinter import scrolledtext

ventana = Tk()
ventana.title("Primoinador")
ventana.geometry('540x480')
ventana.configure(width=540, height=480)
ventana.resizable(False, False)

texto_sup = Label(ventana, text="El Primoinador!", font=("Consolas", 15))
texto_sup.pack()

texto_inf = Label(ventana, text="El ''-inador'' para encontrar números primos", font=("Consolas", 10))
texto_inf.pack()

dsd = Label(ventana, text="Desde el: ", font=("Consolas", 9))
dsd.place(x=98, y=120)

num1_inpt = Entry(ventana, width=10)
num1_inpt.place(x=188, y=120)

hst = Label(ventana, text=" hasta el: ", font=("Consolas", 9))
hst.place(x=278, y=120)

num2_inpt = Entry(ventana, width=10)
num2_inpt.place(x=368, y=120)

act_btn = Button(ventana, text="Encontrar primos")
act_btn.place(x=234, y=180)

rslt = scrolledtext.ScrolledText(ventana, width=40, height=10)
rslt.place(x=117, y=240)
rslt.config(state=DISABLED)

ventana.mainloop()
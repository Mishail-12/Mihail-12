from tkinter import *
from math import *


def proizv():
    a = EntryA.get() 
    a = int(a)
    s = 1
    for i in range(1, a + 1):
        s *= 1 / (i * (i ** 0.5))
    EntryC.delete(0, END) 
    EntryC.insert(0, s)        
        
        
        
def vtoroe():
    b = EntryD.get()
    b = int(b)
    c = EntryD2.get()
    c = int(c)
    p = 1
    for i in range(1, c + 1):
        p += 1 / ((2 * i - 1) * (b ** (2 * i - 1)))
    EntryE.delete(0, END) 
    EntryE.insert(0, p)        
     
        
        
def tri():
    x = float(EntryX.get())
    y = x / ((x ** 4) + (3 * (x ** 2)) + 2)
    EntryY.delete(0, END) 
    EntryY.insert(0, y)           

        
     
root = Tk()


Label(root, text='1)Введите n').grid(row=0, sticky=W)
Label(root, text='Значение Y').grid(row=0, column=4)


EntryA = Entry(root, width=6, font='Arial 16')
EntryC = Entry(root, width=6, font='Arial 16')

EntryA.grid(row=1, sticky=W)
EntryC.grid(row=1, column=4)


but1 = Button(root, text='Найти значение Y', command=proizv)
but1.grid(row=1, column=2)


Label(root, text='2) Введите x').grid(row=4, sticky=W)
Label(root, text='2) Введите n').grid(row=4, column=1)
Label(root, text='Значение z').grid(row=4, column=4)

EntryD = Entry(root, width=6, font='Arial 16')
EntryD.grid(row=5, sticky=W)

EntryD2 = Entry(root, width=6, font='Arial 16')
EntryD2.grid(row=5, column=1)

EntryE = Entry(root, width=6, font='Arial 16')
EntryE.grid(row=5, column=4)

but2 = Button(root, text='Найти значение z', command=vtoroe)
but2.grid(row=5, column=2)


Label(root, text='3)Введите x').grid(row=7, sticky=W)
Label(root, text='Значение функции').grid(row=7, column=5)


EntryX = Entry(root, width=6, font='Arial 16')
EntryX.grid(row=10, sticky=W)

EntryY = Entry(root, width=6, font='Arial 16')
EntryY.grid(row=10, column=5)


but3 = Button(root, text='Найти значение функции', command=tri)
but3.grid(row=10, column=2)

root.mainloop()
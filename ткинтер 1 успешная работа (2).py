from tkinter import *
from math import sin


def proizv():
    a = EntryA.get() 
    a = int(a) 
    if a < 2:
        result = str(a) 
        EntryC.delete(0, END)
        EntryC.insert(0, result) 
    else:
        result = str(2) 
        EntryC.delete(0, END) 
        EntryC.insert(0, result)
        
        
def vtoroe():
    b = EntryD.get()
    b = str(b)
    if b[0] == b[-1]:
        v = 'ДА'
        EntryE.delete(0, END) 
        EntryE.insert(0, v)  
        
    else:
        v = 'НЕТ'
        EntryE.delete(0, END) 
        EntryE.insert(0, v) 
        
        
def tri():
    x = float(EntryX.get())
    y = float(EntryY.get())
    if x ** 2 + y ** 2 >= 4 and x ** 2 <= 4 and y ** 2 <= 4 and (x <= 0 or y <= 0):
        z1 = 'Принадлежит'
        Entry1.delete(0, END) 
        Entry1.insert(0, z1)
    else: 
        z1 = 'Не принадлежит'
        Entry1.delete(0, END) 
        Entry1.insert(0, z1)
    if y > (1 - x) and x >= 0 and y < sin(x):
        z2 = 'Принадлежит'
        Entry2.delete(0, END) 
        Entry2.insert(0, z2)
    else:
        z2 = 'Не принадлежит'
        Entry2.delete(0, END) 
        Entry2.insert(0, z2)
        
        
     
root = Tk()


Label(root, text='1)Введите значение X').grid(row=0, sticky=W)
Label(root, text='Значение Y').grid(row=0, column=4)

EntryA = Entry(root, width=6, font='Arial 16')
EntryC = Entry(root, width=6, font='Arial 16')


EntryA.grid(row=1, sticky=W)


EntryC.grid(row=1, column=4)


but1 = Button(root, text='Найти значение Y', command=proizv)
but1.grid(row=1, column=2)


Label(root, text='2) Введите трехзначное число').grid(row=4, sticky=W)
Label(root, text='Ответ(перевернутое или нет)').grid(row=4, column=4)

EntryD = Entry(root, width=6, font='Arial 16')
EntryD.grid(row=5, sticky=W)

EntryE = Entry(root, width=6, font='Arial 16')
EntryE.grid(row=5, column=4)

but2 = Button(root, text='Найти значение Y', command=vtoroe)
but2.grid(row=5, column=2)


Label(root, text='3)Введите координаты точки').grid(row=7, sticky=W)

Label(root, text='X').grid(row=9, sticky=W)
Label(root, text='Y').grid(row=9, column=1)

EntryX = Entry(root, width=6, font='Arial 16')
EntryX.grid(row=10, sticky=W)

EntryY = Entry(root, width=6, font='Arial 16')
EntryY.grid(row=10, column=1)

Label(root, text='Принадлежность области А').grid(row=12, sticky=W)
Label(root, text='Принадлежность области B').grid(row=12, column=2)

Entry1 = Entry(root, width=6, font='Arial 16')
Entry1.grid(row=13, sticky=W)

Entry2 = Entry(root, width=6, font='Arial 16')
Entry2.grid(row=13, column=2)

but3 = Button(root, text='Определить принадлежности', command=tri)
but3.grid(row=10, column=3)

root.mainloop()
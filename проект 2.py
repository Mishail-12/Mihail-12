from tkinter import *
from PIL import Image

class Program(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.mainmenu = Menu(root)
        root.config(menu=self.mainmenu)
        self.init_main()
        
    def init_main(self):
         
        helpmenu = Menu(self.mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь", command=self.help)
        helpmenu.add_command(label="Об авторе", command=self.name)
        helpmenu.add_command(label="О программе", command=self.prog)
        
        nasmenu = Menu(self.mainmenu, tearoff=0)
        nasmenu.add_command(label="Разрешить разворачивать окно во весь экран", command=self.full)
        nasmenu.add_command(label="Изменить размер формы", command=self.raz)
        nasmenu.add_command(label="Изменить название главного окна", command=self.title)
        

        self.mainmenu.add_cascade(label="Справка", menu=helpmenu)
        self.mainmenu.add_cascade(label="Начать", command=self.kaf)
        self.mainmenu.add_cascade(label="Настройки", menu=nasmenu)
        
        
    def kaf(self):
        Label(self, text='Введите все коэффициенты уравнения через запятую и пробел. Если не знаете как - воспользуйтесь справкой\n').grid(row=0, sticky=W) 
        self.EntryA = Entry(self, width=6, font='Arial 16')
        self.EntryA.grid(row=1, column=0)
        but_res = Button(self, text='Найти все целые корни уравнения', command=self.res)
        but_res.grid(row=1, column=1)
        
        but_graf = Button(self, text='Построить график функции', command=self.graf)
        but_graf.grid(row=2, column=1) 
        
        but_ex = Button(self, text='Найти точки экстремума функции', command=self.ex)
        but_ex.grid(row=3, column=1) 
        
        but_minmax = Button(self, text='Найти точку максимума и точку минимума функции', command=self.minmax)
        but_minmax.grid(row=4, column=1) 
        
    def res(self):
        master = Tk()
        master.title('Корни уравнения')
        de = []
        k = []
        s = str(self.EntryA.get()).split(', ')
        for i in s:
            k.append(int(i))
        h = max(k)
        n = min(k)
        if abs(h) > abs(n):
            m = h
        else:
            m = n
        for i in range(10 * (-abs(m)), 10 * (abs(m) + 1)):
            s = 0
            for g in range(len(k)):
                s += k[g] * (i / 10) ** (len(k) - 1 - g)
            if s == 0:
                de.append(i/ 10)
            s = 0
        if len(de) == 0:
            a = 'Целочисленных корней нет'
        else:
            a = 'Целочисленные корни уравнения'
            for i in de:
                a += str(i) + ', '
        Label(master, text='').grid(row=2, sticky=W)        
        Label(master, text=a).grid(row=2, sticky=W)     
        
    def graf(self):
        k = []
        s = str(self.EntryA.get()).split(', ')
        for i in s:
            k.append(int(i))        
        master = Tk()
        master.title("График функции")
        canvas = Canvas(master, bg='white', height=600, width=600)
        p1 = (0.0, 300.0),
        p2 = (600, 300)
        p3 = (300.0, 0.0),
        p4 = (300, 600)    
        canvas.create_line(p1, p2, fill='black')
        canvas.create_line(p3, p4, fill='black')
        s = []
        for x in range(-300, 300, 1):
            n = 0
            for g in range(len(k)):
                n += k[g] * x ** (len(k) - 1 - g)
            y = -n    
            x1 = 10 * x + 300
            y1 = 10 * y + 300
            f = (x1, y1)
            s.append(f)
        canvas.create_line(*s, fill='red')
        canvas.pack()   
                     
    def ex(self):
        master = Tk()
        master.title('Точки экстремума')
        p = []
        s = str(self.EntryA.get()).split(', ')
        for i in s:
            p.append(int(i))
        k = []
        for i in range(len(p) - 1):
            k.append(p[i] * (len(p) - i - 1))
        h = max(k)
        n = min(k)
        if abs(h) > abs(n):
            m = h
        else:
            m = n
        de = []    
        for i in range(10 *(-abs(m)), 10 * (abs(m) + 1)):
            s = 0
            for g in range(len(k)):
                s += k[g] * (i / 10) ** (len(k) - 1 - g)
            if s == 0:
                de.append(i / 10)
            s = 0
        tochki = []
        y = 0
        for x in de:
            y = 0
            for g in range(len(p)):
                y += p[g] * x ** (len(p) - 1 - g)
            r = (x, y)
            tochki.append(r)
        if len(tochki) != 0:
            a = 'Точки экстремума функции:'
            for i in tochki:
                a += str(i) + ', '
        else:
            a = 'Нет целочисленных точек экстремума функции'
        Label(master, text='').grid(row=2, sticky=W)    
        Label(master, text=a).grid(row=2, sticky=W) 
            
        
                 
    def name(self):
        w = Tk()
        w.title('Об авторе')
        Label(w, text='Автор - Агей Михаил 9В. Прогер-любитель. Лазарусу и Паскалю предпочитет Питон').grid(row=1, sticky=W)
        
    def prog(self):
        w = Tk()
        w.title('О программе')
        Label(w, text='Программа позволяющая найти корни линейного уравнения \nили уравнения высших степеней, его график и точки экстремума. Если автору не будет лень, появится что-нибудь еще.').grid(row=3, sticky=W)
                
    def help(self):
        w = Tk()
        w.title('Помощь')
        Label(w, text='Правило ввода коэффициентов: если старший член многочлена - x ^ n, то нужно ввести (n + 1) коэффициент.\n То есть например для выражения (x^3 - 5x^2 + 10) нужно ввести |1, -5, 0, 10|').grid(row=2, sticky=W) 
          
    def full(self):
        root.resizable(True, True)
        
    def raz(self):
        w = Tk()
        w.title('Изменение размера формы')
        Label(w, text='Введите размер и сдвиг формы').grid(row=2, sticky=W)
        self.EntryR = Entry(w, width=6, font='Arial 16')
        self.EntryR.grid(row=2, column=0)        
        but_r = Button(w, text='Изменить размер формы', command=self.r)
        but_r.grid(row=2, column=1)
        
    def r(self):
        s = str(self.EntryR.get())
        root.geometry(s)
        
    def title(self):
        w = Tk()
        w.title('Изменение названия формы')
        Label(w, text='Введите новое название формы').grid(row=4, sticky=W)
        self.EntryT = Entry(w, width=6, font='Arial 16')
        self.EntryT.grid(row=4, column=0)        
        but_r = Button(w, text='Изменить название формы', command=self.t)
        but_r.grid(row=4, column=1)
        
    def t(self):
        s = str(self.EntryT.get())
        root.title(s)        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Program(root)
    app.grid()
    root.title("Решатель уранений")
    root.geometry("900x400+200+200")
    root.resizable(False, False)     
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askquestion, askyesno

root = Tk()
root.title("Основное меню")
root.iconbitmap(default="ava.ico")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2 - 150
h = h // 2 - 60
root.geometry('360x180+{}+{}'.format(w, h))
colors = ['Red']
a = 10
s = 0
l = 0
v = 0


def Uveren():
    result = askyesno(title="Новая игра", message="Вы уверены что хотите начать новую игру?")
    if result:
        root.destroy()
        newWindow = Tk()
        newWindow.title("Создание бойца")
        newWindow.geometry("360x180")
        l3 = Label(newWindow, text="Настройте своего бойца \n Введите имя бойца")
        l3.place(x=100, y=10)
        en1 = Entry(newWindow, width=30)
        en1.place(x=80, y=50)
        rad1 = Radiobutton(newWindow, text='Мужской', value=1)
        rad1.place(x=100, y=70)
        rad2 = Radiobutton(newWindow, text='Женский', value=2)
        rad2.place(x=180, y=70)
        l3 = Label(newWindow, text="Распределите очки \n Всего очков:")
        l3.place(x=110, y=90)
        l4 = Label(newWindow, text="Сила")
        l4.place(x=80, y=120)
        l5 = Label(newWindow, text="Ловкость")
        l5.place(x=130, y=120)
        l6 = Label(newWindow, text="Стойкость")
        l6.place(x=195, y=120)
        en2 = Entry(newWindow, width=5)
        en2.place(x=80, y=150)
        en3 = Entry(newWindow, width=5)
        en3.place(x=140, y=150)
        en4 = Entry(newWindow, width=5)
        en4.place(x=200, y=150)
        btn4 = Button(text="Начать поединок", width=14, bg="red")
        btn4.place(x=250, y=150)


def Net():
    showinfo(title="Тут ничего нет", message="Ждите в грядущих обновлениях!")


btn = Button(text="Новая Игра!", width=18, bg="red", command=Uveren)
btn.grid(row=2, column=1)
btn2 = Button(text="Продолжить игру", width=18)
btn2.grid(row=3, column=1)
btn3 = Button(text="Настройки игры", width=18, command=Net)
btn3.grid(row=4, column=1)

l1 = Label(text="Добро пожаловать!", width=50, fg="red")
l1.grid(row=1, column=1, columnspan=1)
l2 = Label(text="Разработчики: \n Роман Горин \n Демшин Станислав \nАртамонов Даниил", width=50, anchor=W)
l2.grid(row=5, column=1, columnspan=1)
root.mainloop()


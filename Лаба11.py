# Практика 11
# Создание GUI
from tkinter import *
from tkinter import messagebox, filedialog

window = Tk()
window.title("Герасимов Денис Павлович")
window.geometry("800x480")


# Задание 1
num1 = Label(window,
            text="Задание 1",
            font=("Arial Bold", 11),
            width=20, height=2
            )
num1.grid(column=0, row=0)
lbl1 = Label(window,
            text="Калькулятор",
            font=("Arial Bold", 14),
            width=20, height=2
            )
lbl1.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt1.grid(column=0, row=2)

txt2 = Entry(window, width=10)
txt2.grid(column=0, row=3)

opvar = StringVar()
opvar.set("+")

oper = ["+", "-", "*", "/"]
opmenu = OptionMenu(window, opvar, *oper)
opmenu.grid(column=0, row=4)

oplbl = Label(window,
              text="Вывод:",
              font=("Arial Bold", 12),
              width=20, height=2
              )
oplbl.grid(column=0, row=5)


def calculator():
    a = float(txt1.get())
    b = float(txt2.get())
    op = opvar.get()
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a // b

    oplbl.config(text=f"Вывод: {res}")

calc = Button(window,
              text="ОТВЕТ",
              command = calculator
              )
calc.grid(column=0, row=6)


# Задание 2
num2 = Label(window,
             text="Задание 2",
             font=("Arial Bold", 11),
             width=20, height=2
             )
num2.grid(column=3, row=0)

lbl2 = Label(window,
             text="Чекбоксы",
             font=("Arial Bold", 14),
             width=20, height=2)
lbl2.grid(column=3, row=1)


chk_var1 = BooleanVar()
chk_var2 = BooleanVar()
chk_var3 = BooleanVar()

chk1 = Checkbutton(window,
                  text="Первый",
                  variable=chk_var1
                  )
chk1.grid(column=3, row=2)

chk2 = Checkbutton(window,
                   text="Второй",
                   variable=chk_var2
                   )
chk2.grid(column=3, row=3)

chk3 = Checkbutton(window,
                   text="Третий",
                   variable=chk_var3
                   )
chk3.grid(column=3, row=4)

def ckbox():
    select = []
    if chk_var1.get():
        select.append("Первый")
    elif chk_var2.get():
        select.append("Второй")
    elif chk_var3.get():
        select.append("Третий")

    if select:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(select)}")
    else:
        messagebox.showinfo("Выбор", "Ничего")

chk_btn = Button(window,
                text="Показать",
                command=ckbox
                )
chk_btn.grid(column=3, row=5)


# Задание 3
num3 = Label(window,
             text="Задание 3",
             font=("Arial Bold", 11),
             width=20, height=2
             )
num3.grid(column=6, row=0)

lbl3 = Label(window,
             text="Текст",
             font=("Arial Bold", 14),
             width=20, height=2
             )
lbl3.grid(column=6, row=1)

text3 = Text(window,
             width=30, height=1)
text3.grid(column=6, row=2)


def menu():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            text3.delete(1.0, END)
            text3.insert(1.0, text)
        messagebox.showinfo("Успешно", "Файл импортирован")

    else:
        messagebox.showinfo("Ошибка", "Не вышло")


byn_load = Button(window,
                  text="Загрузить файл",
                  command=menu
                  )
byn_load.grid(column=6, row=3)

window.mainloop()
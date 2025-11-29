# Практика 11
# Создание GUI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog

window = Tk()
window.title("Герасимов Денис Павлович")
window.geometry("420x420")


notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=1)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Калькулятор')

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Чекбоксы')

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Текст из файла')


# Задание 1
lbl1 = Label(tab1,
            text="Калькулятор",
            font=("Arial Bold", 14),
            width=20, height=3
            )
lbl1.grid(column=20, row=0)

txt1 = Entry(tab1, width=10)
txt1.grid(column=20, row=1)

txt2 = Entry(tab1, width=10)
txt2.grid(column=20, row=2)

opvar = StringVar()
opvar.set("+")

oper = ["+", "-", "*", "/"]
opmenu = OptionMenu(tab1, opvar, *oper)
opmenu.grid(column=20, row=3)

oplbl = Label(tab1,
              text="Вывод:",
              font=("Arial Bold", 12),
              width=45, height=3
              )
oplbl.grid(column=20, row=4)


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
        res = a / b

    oplbl.config(text=f"Вывод: {res}")


calc = Button(tab1,
              text="ОТВЕТ",
              command = calculator
              )
calc.grid(column=20, row=5)


# Задание 2
lbl2 = Label(tab2,
             text="Чекбоксы",
             font=("Arial Bold", 14),
             width=35, height=2)
lbl2.grid(column=3, row=0)


chk_var1 = BooleanVar()
chk_var2 = BooleanVar()
chk_var3 = BooleanVar()


chk1 = Checkbutton(tab2,
                  text="Первый",
                  variable=chk_var1
                  )
chk1.grid(column=3, row=1)

chk2 = Checkbutton(tab2,
                   text="Второй",
                   variable=chk_var2
                   )
chk2.grid(column=3, row=2)

chk3 = Checkbutton(tab2,
                   text="Третий",
                   variable=chk_var3
                   )
chk3.grid(column=3, row=3)

def ckbox():
    select = []
    if chk_var1.get():
        select.append("Первый")
    if chk_var2.get():
        select.append("Второй")
    if chk_var3.get():
        select.append("Третий")

    if select:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(select)}")
    else:
        messagebox.showinfo("Выбор", "Ничего")

chk_btn = Button(tab2,
                text="Показать",
                command=ckbox
                )
chk_btn.grid(column=3, row=4)


# Задание 3
lbl3 = Label(tab3,
             text="Текст",
             font=("Arial Bold", 14),
             width=35, height=2
             )
lbl3.grid(column=6, row=0)

text3 = Text(tab3,
             width=30, height=10)
text3.grid(column=6, row=1)


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


byn_load = Button(tab3,
                  text="Загрузить файл",
                  command=menu
                  )
byn_load.grid(column=6, row=2)

window.mainloop()

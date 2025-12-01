import json
import requests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Инфа из GIT")
window.geometry("800x460")

label = tk.Label(window,
                 text='Введите имя пользователя',
                 font=('Calibri Bold', 16)
                 )
label.pack(pady=20)

entry = tk.Entry(window,
                 width=40,
                 font=('Calibri', 12)
                 )
entry.pack(pady=10)

res_text = tk.LabelFrame(window,
                    text="Результат",
                    font=('Calibri Bold', 12),
                    padx=10,
                    pady=10
                    )
res_text.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

res = tk.Text(res_text,
              width=40,
              height=2,
              font=('Calibri', 12)
              )
res.pack(fill=tk.BOTH, expand=True)


def infa():
    username = entry.get()
    if username =="":
        messagebox.showwarning("Ошибка", "Введите username")
        return

    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        result = {
            'company': data.get('company'),
            'created_at': data.get('created_at'),
            'email': data.get('email'),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('url'),
        }

        res.delete(1.0, tk.END)
        res.insert(1.0, json.dumps(result, indent=2))

        with open(f'fithub_{username}.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        messagebox.showinfo("Успешно", "Данные импортированы!")
    else:
        messagebox.showerror("Ошибка", "Не найден!")

button = tk.Button(window,
                   text="Получить",
                   command=infa,
                   font=('Calibri', 12)
                   )
button.pack(pady=10)

window.mainloop()

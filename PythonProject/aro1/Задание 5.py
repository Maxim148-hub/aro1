from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox as mb


def update_base_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)


def update_base2_label(event):
    # Получаем полное название второй базовой валюты из словаря и обновляем метку
    code = base2_combobox.get()
    name = currencies[code]
    b2_label.config(text=name)


def update_target_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

window = Tk()
window.title("Курс обмена валюты")
window.geometry('400x600+600+300')

Label(text="Первая базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", update_base2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Сравнить курсы обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
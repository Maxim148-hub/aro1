from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry('400x300+600+300')

# Выбор криптовалюты
Label(text="Выберите криптовалюту:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox()
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>")

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

# Целевая валюта
Label(text="Американский доллар:").pack(padx=10, pady=5)
Label(text="USD").pack(padx=10, pady=5)


# Кнопка для получения курса
Button(text="Курс обмена").pack(padx=10, pady=20)




window.mainloop()


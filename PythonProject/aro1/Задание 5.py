from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox as mb



window = Tk()
window.title("Курс обмена валюты")
window.geometry('400x600+600+300')

Label(text="Первая базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", )

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list())
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", )

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list())
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", )

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Сравнить курсы обмена", ).pack(padx=10, pady=10)

window.mainloop()
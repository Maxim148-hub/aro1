from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


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


def exchange():
    base_code = base_combobox.get()
    base2_code = base2_combobox.get()
    target_code = target_combobox.get()

    if target_code and base_code and base2_code:
        try:
            # Получаем курс для первой базовой валюты
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response1.raise_for_status()
            data1 = response1.json()

            # Получаем курс для второй базовой валюты
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()
            data2 = response2.json()

            if target_code in data1['rates'] and target_code in data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]

                base = currencies[base_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]

                # Сравнение курсов
                mb.showinfo("Курс обмена",
                            f"Курс {base}: {exchange_rate1:.2f} {target} за 1 {base}\n"
                            f"Курс {base2}: {exchange_rate2:.2f} {target} за 1 {base2}")

            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")

        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")

    else:
        mb.showwarning("Внимание", "Выберите все валюты")


# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry('400x600+600+300')

# Первая базовая валюта
Label(text="Первая базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

# Вторая базовая валюта
Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", update_base2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)

# Целевая валюта
Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

# Кнопка для получения курса
Button(text="Сравнить курсы обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
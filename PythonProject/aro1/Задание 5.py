from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox as mb


def exchange():
    url = "https://api.exchangerate-api.com/v4/latest/RUB"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rates = data.get('rates',{})

        usd_rate = rates.get('USD')
        eur_rate = rates.get('EUR')
        rub_rate = rates.get('RUB')

        if usd_rate and eur_rate:

            eur = f"1 EUR = {(rub_rate / eur_rate):.2f} RUB"
            usd = f"1 USD = {(rub_rate / usd_rate):.2f} RUB"

            mb.showinfo('Курсы валют:', f'{eur}\n{usd}')

    except requests.exceptions.RequestException as e:
        mb.showerror(f"Ошибка при запросе к API: {e}")
    except ValueError as e:
        mb.showerror(f"Ошибка обработки данных: {e}")


loot = Tk()
loot.title("Курсы обмена валют")
loot.geometry('400x500+600+300')

s = Label(loot, text = 'Базовая валюта')
s.pack(side='top', pady=20)

frame = Frame(loot)
frame.pack()

window = Entry(frame,width=20)
window.grid()

combo = ttk.Combobox(window)
combo.pack()
combo.set("EUR")

s1 = Label(loot, text = 'Евро')
s1.pack(side='top', pady=10)

s2 = Label(loot, text = 'Вторая базовая валюта')
s2.pack(side='top', pady=30)

frame1 = Frame(loot)
frame1.pack()

window1 = Entry(frame1, width=20)
window1.grid()

combo = ttk.Combobox(window1)
combo.pack()
combo.set("USD")

s3 = Label(loot, text = 'Американский доллар')
s3.pack(side='top', pady=10)

s4 = Label(loot, text = 'Целевая валюта')
s4.pack(side='top', pady=30)

frame2 = Frame(loot)
frame2.pack()

window2 = Entry(frame2, width=20)
window2.grid()

combo = ttk.Combobox(window2)
combo.pack()
combo.set("RUB")

s4 = Label(loot, text = 'Российский рубль')
s4.pack(side='top', pady=10)

add = Button(loot,command=exchange)
add.config(width=20, text='Получить курс обмена', justify='center')
add.pack(pady=30)

loot.mainloop()

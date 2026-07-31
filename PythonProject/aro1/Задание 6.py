from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_base_label(event):
    # Получаем название криптовалюты из словаря и обновляем метку
    code = base_combobox.get()
    name = coin_ids[code]
    b_label.config(text=name)


def exchange():
    base_code = base_combobox.get()

    if not base_code:
        mb.showwarning("Ошибка", "Выберите криптовалюту")
        return

    try:
        # Получаем курс криптовалюты
        coin_id = coin_ids[base_code]
        response = requests.get(
            f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd')
        response.raise_for_status()
        data = response.json()

        base = coin_id[base_code]
        if base_code in data['coin_id']:
            exchange_rate1 = data['coin_id']['usd']
            base = coin_id[base_code]

            # Сравнение курсов
            mb.showinfo("Курс обмена",
                        f"1 {base} = {exchange_rate1:.2f},{base},USD")

        else:
            mb.showerror("Ошибка", f"Валюта {base} не найдена")

    except Exception as e:
        mb.showerror("Ошибка", f"Ошибка: {e}")


# Словарь кодов популярных криптовалют и их названий
coin_ids  = {
    "BTC" :  "Bitcoin",
    "ETH" :  "Ethereum",
    "USDT":  "Tether",
    "BNB" :  "BNB",
    "XRP" :  "XRP",
    "USDC":  "USD Coin",
    "SOL" :  "Solana",
    "TRX" :  "TRON",
    "DOGE":  "Dogecoin",
    "ADA" :  "Cardano",
    "STETH": "Lido Staked Ether",
    "BCH" :  "Bitcoin Cash",
    "LINK":  "Chainlink",
    "SUI" :  "Sui",
    "HYPE":  "Hyperliquid"
}

window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry('400x300+600+300')

# Выбор криптовалюты
Label(text="Выберите криптовалюту:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(coin_ids.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

# Целевая валюта
Label(text="Американский доллар:").pack(padx=10, pady=5)
Label(text="USD").pack(padx=10, pady=5)


# Кнопка для получения курса
Button(text="Текущий курс обмена", command=exchange).pack(padx=10, pady=20)




window.mainloop()


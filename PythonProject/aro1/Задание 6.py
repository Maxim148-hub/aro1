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
        mb.showwarning("Внимание", "Выберите криптовалюту")
        return

    try:
        if base_code not in coin_ids:
            mb.showerror("Ошибка", f"Криптовалюта {base_code} не поддерживается")
            return

        coin_id = coin_ids[base_code]
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if coin_id in data and 'usd' in data[coin_id]:
            exchange_rate = data[coin_id]['usd']
            base_name = coin_ids[base_code]

            mb.showinfo("Курс обмена",
                        f"1 {base_name} = {exchange_rate:.2f} USD")
        else:
            mb.showerror("Ошибка", f"Не удалось получить курс для {base_code}")

    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка соединения", f"Не удалось подключиться к API: {e}")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


# Словарь кодов популярных криптовалют и их названий
coin_ids = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDT": "tether",
    "BNB": "binancecoin",
    "XRP": "ripple",
    "USDC": "usd-coin",
    "SOL": "solana",
    "TRX": "tron",
    "DOGE": "dogecoin",
    "ADA": "cardano",
    "STETH": "staked-ether",
    "BCH": "bitcoin-cash",
    "LINK": "chainlink",
    "SUI": "sui",
    "HYPE": "hyperliquid"
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
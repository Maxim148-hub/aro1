from tkinter import *
from tkinter import ttk

loot = Tk()
loot.title("Курсы обмена валют")
loot.geometry('400x500+600+300')


s = Label(loot, text = 'Базовая валюта')
s.pack(side='top', pady=10)

frame = Frame(loot)
frame.pack(pady=10)

window = Entry(frame, width=20,font=('Arial',12))
window.grid()

s1 = Label(loot, text = 'Евро')
s1.pack(side='top', pady=10)

s2 = Label(loot, text = 'Вторая базовая валюта')
s2.pack(side='top', pady=10)

frame1 = Frame(loot)
frame1.pack(pady=10)

window1 = Entry(frame1, width=20,font=('Arial',12))
window1.grid()

s3 = Label(loot, text = 'Американский доллар')
s3.pack(side='top', pady=10)

s4 = Label(loot, text = 'Целевая валюта')
s4.pack(side='top', pady=10)

frame2 = Frame(loot)
frame2.pack(pady=30)


window2 = Entry(frame2, width=20,font=('Arial',12))
window2.grid()

s4 = Label(loot, text = 'Российский рубль')
s4.pack(side='top', pady=10)

add = Button(loot)
add.config(width=20, text='Получить курс обмена', justify='center',font=('Arial',10))
add.pack()

loot.mainloop()

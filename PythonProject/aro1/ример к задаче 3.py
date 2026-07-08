from tkinter import *
from tkinter import messagebox as mb

def sum():
    s1 = window1.get()
    s2 = window2.get()
    s3 = window3.get()
    try:
        slag1 = float(s1)
    except ValueError:
        mb.showerror("Ошибка", "В первом поле должно быть введено число")
        return

    try:
        slag2 = float(s2)
    except ValueError:
        mb.showerror("Ошибка", "Во втором поле должно быть введено число")
        return

    try:
        slag3 = float(s3)
    except ValueError:
        mb.showerror("Ошибка", "В третьем поле должно быть введено число")
        return


    summa = slag1 + slag2 + slag3


    if summa.is_integer():
        summa_text = str(int(summa))
    else:
        summa_text = str(summa)
        mb.showinfo('Результат:', summa_text)


def mot():
    sum()
    # s1 = window1.get()
    # s2 = window2.get()
    # s3 = window3.get()
    # try:
    #     slag1 = float(s1)
    # except ValueError:
    #     mb.showerror("Ошибка", "В первом поле должно быть введено число")
    #     return
    #
    # try:
    #     slag2 = float(s2)
    # except ValueError:
    #     mb.showerror("Ошибка", "Во втором поле должно быть введено число")
    #     return
    #
    # try:
    #     slag3 = float(s3)
    # except ValueError:
    #     mb.showerror("Ошибка", "В третьем поле должно быть введено число")
    #     return
    work = slag1 * slag2 * slag3

    if work.is_integer():
        work_text = str(int(work))
    else:
        work_text = str(work)
    mb.showinfo('Результат:', work_text)



loot = Tk()
WIDIH = loot.winfo_screenwidth()
HEIGHT = loot.winfo_screenheight()

loot.title('Калькулятор')
loot.geometry(f'400x250+{WIDIH//2-400//2}+'
               f'{HEIGHT//2-250//2-100}')

s = Label(loot, text = 'Введите три числа и нажмите на кнопку для вычеслений')
s.pack(side=TOP, pady=10)
s.config(font = ('Arial',10))
frame = Frame(loot)
frame.pack(pady=10)

window1 = Entry(frame, width=10,font=('Arial',15),justify='center')
window1.grid()
window2 = Entry(frame, width=10,font=('Arial',15),justify='center')
window2.grid()
window3 = Entry(frame, width=10,font=('Arial',15),justify='center')
window3.grid()

add = Button(loot)
add.config(width=14, text='Сложить три числа', justify='center',font=('Arial',10), command=sum)
add.pack()

mult = Button(loot)
mult.config(width=15, text='Умножить три числа', justify='center',font=('Arial',10),command=mot)
mult.pack()

loot.mainloop()
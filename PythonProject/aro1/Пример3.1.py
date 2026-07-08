from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    s2 = e2.get()
    s3 = e3.get()
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
    # if not s3.lstrip('-').isdigit():
    #     mb.showerror("Ошибка", "В третье поле должно быть введено число")
    #     return  # Возвращаемся из функции, если ввод некорректен


    # slag1 = float(s1)
    # slag2 = int(s2)
    # slag3 = int(s3)

    summa = slag1 + slag2 + slag3


    if summa.is_integer():
        summa_text = str(int(summa))
    else:
        summa_text = str(summa)
    mb.showinfo('Результат:', summa_text)
    # m1['text'] = f"{s1} + {s2} + {s3} = {str(summa)}"
    #
    # answer = mb.askretrycancel(title="Вопрос", message="Сложить еще три числа?")
    #
    # if answer:
    #
    #     e1.delete(0, END)
    #     e2.delete(0, END)
    #     e3.delete(0, END)
    #
    #     m1['text'] = ""
    #
    # else:
    #
    #     window.destroy()

window = Tk()
window.title("Калькулятор")

m = Label(height=3, text="Введите три числа и нажмите на кнопку для вычисления суммы")
m.pack()

e1 = Entry()

e1.pack()

e2 = Entry()

e2.pack()

e3 = Entry()  # Добавление третьего поля для ввода

e3.pack()

b = Button(text="Сложить три числа", command=summ)

b.pack()

m1 = Label(height=3)

m1.pack()

window.mainloop()

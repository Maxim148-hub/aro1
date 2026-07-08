from datetime import datetime, date, timedelta, time, UTC

# t = time(12)
# # t = time(25)  # будет ошибка нельзя вводить время вне диапазона
# print(t)
# t = time(12, 30)
# print(t)
# t = time(12, 30,15)
# print(t)
# d = date(2020, 12, 31)  # соблюдаем порядок год, месяц, день
# print(d)
# d = date(2026, 3, 23)
# dd = date.today()
# print(dd)
# # dt = dd + time  - нельзя разные типы данных
# dt = datetime.combine(dd, t)
# print(dt)
# print(dd - d)
# current_date = datetime.now()  # получаем текущее время и дату
# print(current_date)
# inp_date = input('Введите дату (дд.мм.гггг): ')
# print(inp_date)
# dt = datetime.strptime(inp_date, '%d.%m.%Y')  # перевод из строкового типа в datetime
# print(dt)
# print((current_date - dt))  # определяем количество дней между датами
# print((current_date - dt).days)  # преобразуем timedelta в число (int) дней
# print(type((current_date - dt).days))
# curr_date_str = current_date.strftime('%d.%m.%Y')  # перевод из datetime в строку
# print(curr_date_str)
# print(datetime.strptime('12/03/1948 16:44', '%d/%m/%Y %H:%M'))

# print(current_date.strftime('%A %d %B %Y %I:%M %p '))
# print(current_date.strftime('%A %d %B %Y %H:%M:%S.%f'))
# print(current_date.strftime('%A %d %B %Y %X'))
# print(current_date.strftime('%A %d %B %y %x'))
# print(current_date.replace(year=2033, microsecond=0))
# print(datetime.today())
# print(datetime.utcnow())  #  уже устаревшая форма получения мирового времени
# print(datetime.now(UTC))  # Надо импортировать UTC
# tt = current_date.timetuple()
# # print(tt)
# for i in tt:
#     print(i)
# print(current_date.weekday())  # номер дня недели начиная 0(понедельник)
# print(current_date.isoweekday())  # номер дня недели начиная 1(понедельник)
# print(current_date.isocalendar())  # получаем год, неделя месяца, день недели по ISO

# days_of_week = ['Пн', 'Вт','Ср','Чт','Пт','Сб','Вс']
# print(days_of_week[current_date.weekday()])
# months = ['','Янв','Фев','Март','Апр','Май','Июнь','Июль']
# print(months[current_date.month])

# расчет дней до ДР
birthdate = input('ВВедите дату рождения (дд.мм.гггг): ')
birthdate = datetime.strptime(birthdate, '%d.%m.%Y')  # из str в datetime
birthdate = birthdate.date()  # из datetime в date
current_date = date.today()
yyear = current_date.year
birthday = birthdate.replace(year=yyear)  # Замена в дате рождения года на текущий
if current_date > birthday:
    birthday = birthday.replace(year=yyear + 1)  # увеличиваю значение года, если ДР уже было
elif current_date == birthday:
    print(f'Поздравляем')
    exit(0)
amount_days = (birthday - current_date)

print(f' До дня рождения осталось {amount_days.days} дней/дня')


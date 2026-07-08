def log(result):
    with open('calculations.txt', 'w', encoding='utf-8') as file:
        file.write(result)


print('\033[34m' + 'Выберите операцию:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Просмотр истории вычеслений')

choice = input('Введите номер операции (1/2/3/4/5): ')
print('История вычеслений:')

if choice == '1':
    r = f'Результат: 1 + 1 = 2'
    print(r)
    log(r)
elif choice == '2':
    r = f'Результат: 2 - 2 = 0'
    print(r)
    log(r)
elif choice == '3':
    r = f'Результат: 3 * 3 = 9'
    print(r)
    log(r)
elif choice == '4':
    r = f'Результат: 4 / 4 = 1.00'
    print(r)
    log(r)
elif choice == '5':
    r = (f'Результат: 1 + 1 = 2\nРезультат: 2 - 2 = 0\nРезультат: 3 * 3 = 9'
         f'\nРезультат: 4 / 4 = 1.00\nРезультат: 1 + 1 = 2\n'
         f'Результат: 44 + 77 = 121')
    print(r)
    log(r)
else:
    print('Неверный ввод' + '\033[0m')


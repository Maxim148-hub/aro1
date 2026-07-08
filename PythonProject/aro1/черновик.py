

# text = ('Python - современный язык програмирования! Многие начинают изучать '
#      'Python! Мыуже пишим код на Python!!!')
#
# new_text = text.replace('Python','Java' )
# print(new_text)
# new_text = text.replace('!',' ' )
# print(new_text)
# new_text = text.upper()
# print(new_text)

# Задание 2
# while True:
#     password = input('Введите пароль: ')
#     has_upper = False
#     has_digit = False
#
#     for i in password:
#         if i.isupper():
#             has_upper = True
#         if i.isdigit():
#             has_digit = True
#
#     if len(password) >= 8 and has_upper and has_digit:
#         print('Ваш пароль принят!')
#         break
#
#     else:
#         print('Пароль не соответствует требованиям! ')


# numbers = [12,7,18,5,9,14,21,8,30,11,4,15]
# print(numbers[2::2])
#
# print(numbers[::-1])
# num_new = ()
# for i in numbers:
#     i % 3 != 0
#     print(num_new(i), end = ' ')



# fruits = ('яблоко','банан','груша','апельсин','банан','киви','банан','слива')
# print(fruits.index('банан'))
#
# print(fruits.count('банан'))
# fruits1 =()
# for i in fruits:
#     fruits1 += (i,i)
# print(fruits1)

# set1 = {2,4,6,8,10,12}
# set2 = {6,8,10,14,16,18}
#
#
# res = set1.intersection(set2)
# print(res)
#
# set4 = set1 | set2
# print(set4)
#
# set5 = set1 - set2
# print(set5)
# print(set1.issubset(set2))

# d = {'Иван':[5,4,5],'Петр':[3,4,4],'Мария':[5,5,4],'Ольга':[4,5,5]}
# d1 = {'Елена':[5,4,5],'Дмитрий':[3,4,4],'Сергей':[5,5,4]}
#
# d['Анна'] = [5,5,5]
# print(d)
#
# del d['Петр']
# print(d)
# for k,v in d.items():
#     average  = round(sum(v)/len(v))
#     print(k,average)
#
# d.update(d1)
# print(d)

# import random
#
# secret_number = random.randint(1,100)
# print(secret_number)
# count = 0
#
# while True:
#     yor_number = int(input('Введите число: '))
#     count += 1
#
#     if yor_number < secret_number:
#         print('Больше')
#     elif yor_number > secret_number:
#         print('Меньше')
#     else:
#         print(f'Поздравляю! Вы угадали число{secret_number} с {count} попытки ')
#         break



st = input('Введите строку: ')

vowels = ' а,е,ё,и,о,у,ы,э,ю,я '
print (type(vowels))

vowels = [i.strip() for i in vowels.split(',')]
print(vowels)

count_vowels = 0
count_con = 0
count_digit = 0

for i in st:
    if i in vowels:
        count_vowels += 1
    elif i.isalpha():
        count_con += 1
    elif i.isdigit():
        count_digit += 1

max_count = 0
max_ch = ' '
count = 0
for i in st:
    if i != ' ':
        count = st.count(i)
    if count > max_count:
        max_count = count
        max_ch = i



print(f'Количество гласных букв {count_vowels}\n'
      f'количество согластных {count_con}\n'
      f'количество цифр {count_digit}\n'
      f'самыйвстречающийся  символ {max_ch} \n'
      f'стречается в строке { max_count} раза ')

















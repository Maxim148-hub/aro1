


import random as rd

nums = [22,33,44,55,66,77,88,99]
names = ['Dasha', 'Sasha','Glasha','Masha','Andre']


workers = 6

months = 3

salary = [rd.choices(range(60, 151, 5), k=months) for _ in range(workers)]

# for w in range(workers):

#     salary.append(rd.choices(range(60, 151, 5), k=months))

#     for m in range(months):

#         salary[w].append(rd.randint(60, 150))

# print(salary)

print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'* 22}{chr(2930)}{'-'* 7} {chr(2930)}')

print(f'{chr(2930)}  Работники {chr(2930)} ', end='')

for i in range(months):

    print(f'{i + 1} мес.', end=chr(2930) + ' ')

print(f'{' Итого'} {chr(2930)}')

print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'* 22}{chr(2930)}{'-'* 7} {chr(2930)}')

itog =[0]* months

for k, i in enumerate(salary):

    print(f'{chr(2930)}   {k+1} сотр.  ', end=chr(2930) + ' ')

    for n, j in enumerate(i):

        itog[n] += j

        print(f' {j:4} ', end=chr(2930) + ' ')

    print(f'{sum(i):5} {chr(2930)}')

print(f'{chr(2930)}    Итого   {chr(2930)} ', end='')

for i in itog:

    print(f'{i: 5} ', end=chr(2930) + ' ')

print(f' {sum(itog)} {chr(2930)}')
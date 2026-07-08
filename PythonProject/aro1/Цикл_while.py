# n = int(input('> '))
# while n !=0:
#     print(n)
#     n = int(input('> '))

# n = int(input('> '))
# sm = 0
# count = 0
# while n != 0:
#     sm += n
#     count  += 1
#     n = int(input('>> '))
# print(f'Сумма:{sm}, количество: {count}')

# prod = input('Заберите продукт: ')
# refr = ""
# count = 0
# while prod.lower() != "stop":
#     refr += prod + ' '
#     count += 1
#     prod = input('Заберите продукт: ')
# res = refr.split()
# for product in res:
#     print(product)

# n = int(input('> '))
# nn = n
# sm = 0
# cnt =0
# while n > 0:
#     rem = n % 10
#     sm += rem
#     cnt += 1
#     n = n // 10
# print(f'в числе "{nn}" {cnt} ц. суммщй {sm}')

n = int(input('> '))
res = 0
while n > 0:
    rem = n % 10
    res = res * 10 + rem
    n //= 10  # получение целой части от деления
print(res)






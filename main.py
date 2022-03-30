from functools import lru_cache
import sys

"""import datetime

now = datetime.datetime.now()
o_now = now.strftime('%H:%M:%S')

while True:
    now = datetime.datetime.now()
    now_time = now.strftime('%H:%M:%S')

    if o_now != now_time:
        o_now = now_time
        print(o_now)

weight = int(input('Введите вес: '))
height = int(input('Введите рост: '))

index = weight / (height/100)**2

if index > 25:
    print(f'Поздравляю! Ты жирный. Твой индекс массы тела: {round(index, 2)}')
elif index < 18.5:
    print(f'Поздравляю! Ты дрыщ. Твой индекс массы тела: {round(index, 2)}')
else:
    print(f'Все норм. Твой индекс массы тела: {round(index, 2)}')"""

n = int(input('Введите n: '))
p = 1
q = 1
ans = 1
"""for i in range(n-2):
    ans = p + q
    p = q
    q = ans
    print(ans)"""

sys.setrecursionlimit(5000)


@lru_cache()
def fibo(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibo(i - 1) + fibo(i - 2)


"""for x in range(1, n + 1):
    ans *= x"""


@lru_cache()
def fact(j):
    if j < 2:
        return 1
    return fact(j - 1) * j


print(fact(n))

import math

'''len_str = round(math.pi * d, 2)
s_str = round(math.pi * d ** 2, 2)

w_strip = round(w_led * count_led * (len_str/100), 2)

print(f'Длинна окружности: {len_str} см')
print(f'Площадь окржности: {s_str} см2')
print(f'Требуемая мощность: {w_strip} Вт')'''


class Watt:
    def __init__(self, diam, c_led):
        self.w_led = 0.24
        self.d = diam if diam > 0 else 1
        self.count_led = c_led if c_led == 30 or c_led == 60 or c_led == 120 else 1

    def wolt(self):
        len_str = round(math.pi * d, 2)
        s_str = round(math.pi * d ** 2, 2)
        w_strip = round(w_led * count_led * (len_str / 100), 2)
        ans = f'Длинна окружности: {len_str} см\nПлощадь окржности: {s_str} см2\nТребуемая мощность: {w_strip} Вт '
        return ans


d = float(input('Введите диаметр: '))
w_led = 0.24
count_led = int(input('Введите кол-во светодиодов (30, 60, 120): '))
flag = False
while not flag:
    if count_led == 30 or count_led == 60 or count_led == 120:
        flag = True
    else:
        print('Вы некоректно ввели количество светодиодов')
        count_led = int(input('Введите кол-во светодиодов (30, 60, 120): '))

watt = Watt(d, count_led)
print(watt.wolt())

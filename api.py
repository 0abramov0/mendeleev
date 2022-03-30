import requests
import datetime
import time

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
now = datetime.datetime.now()
r = requests.get(url)
cur = r.json()

old_info_usd = cur["Valute"]["USD"]["Value"]
old_info_euro = cur["Valute"]["EUR"]["Value"]

while True:
    r_new = requests.get(url)
    cur_new = r_new.json()

    cur_usd = cur_new["Valute"]["USD"]["Value"]
    cur_euro = cur_new["Valute"]["EUR"]["Value"]
    usd_flag = False
    euro_flag = False

    print(cur_usd)
    print(f'{cur_euro}\n')

    if cur_usd != old_info_usd:
        old_info_usd = cur_usd
        usd_flag = True
    elif cur_euro != old_info_euro:
        old_info_euro = cur_euro
        euro_flag = True

    cur_time = now.strftime('%H:%M:%S')

    if usd_flag and euro_flag:
        print(cur_time)
        print(f'Курс доллара: {old_info_usd}')
        print(f'Курс евро: {old_info_euro}\n')
    elif usd_flag and not euro_flag:
        print(cur_time)
        print(f'Курс доллара: {old_info_usd}')
    elif euro_flag and not usd_flag:
        print(cur_time)
        print(f'Курс евро: {old_info_euro}\n')

    time.sleep(1)

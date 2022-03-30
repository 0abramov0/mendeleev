import requests
import time

url = 'http://api.forismatic.com/api/1.0/'
params = {'method': 'getQuote', 'key': '457653', 'format': 'json', 'lang': 'ru'}


while True:
    result = requests.get(url, params=params)
    quote = result.json()

    print(str(quote["quoteText"]))
    print(f'{str(quote["quoteAuthor"])}\n')
    time.sleep(2)

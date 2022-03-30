import requests
from bs4 import BeautifulSoup
import re

url = 'https://news.mail.ru/coronavirus/stat/region/72/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

script = str(soup.find('body').find('div', {"class": "layout"}).find_all('script')[8])

region = str(re.findall(r'"region":(.+)', script))
t1 = int(str(re.findall(r'"delta_confirmed":"([^"]+)', region))[2:-2].replace(' ', ''))

print(t1)

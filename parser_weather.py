#
from bs4 import BeautifulSoup
import requests
url='https://pogoda.mail.ru/prognoz/chelyabinsk/'
response = requests.get(url)
print(response)
bs = BeautifulSoup(response.text,'lxml')
temp=bs.find('div','information__content__temperature')
print(temp.text)

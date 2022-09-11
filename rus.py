import requests

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

text = response.content.decode('cp1251')

with open('russian.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian_surnames.txt')

text = response.content.decode('cp1251')

with open('russian_surnames.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))
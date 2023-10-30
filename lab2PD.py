import requests
import json
import csv
import datetime
import webbrowser


def get_exchange_rate(url):
    response = requests.get(url)
    data = json.loads(response.content)

    # Проверка корректности данных
    if 'USD' not in data['rates']:
        raise ValueError('Не удалось найти курс доллара в данных')

    # Обработка ошибок
    try:
        return data['rates']['USD']
    except KeyError:
        raise ValueError('Курс доллара не найден в данных')
    except json.JSONDecodeError:
        raise ValueError('Не удалось декодировать данные JSON')


def save_exchange_rate(rate, date):
    with open('dataset.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([date, rate])


def get_exchange_rate_for_currency(url, currency):
    # Получаем курс валюты
    rate = get_exchange_rate(url)

    # Сохраняем курс валюты в выходной файл
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    save_exchange_rate(rate, date)


def add_github_link(filename):
    with open(filename, 'a') as f:
        f.write('[Github](https://github.com/bard/get_exchange_rate)\n')


def open_link(link):
    webbrowser.open(link)


if __name__ == '__main__':
    # Получаем курс доллара по максимально возможному периоду
    start_date = '2023-01-01'
    end_date = '2023-10-09'
    url = f'https://www.cbr-xml-daily.ru/archive/{start_date}/{end_date}/daily.json.js'
    get_exchange_rate_for_currency(url, 'USD')

    # Получаем курс евро по максимально возможному периоду
    url = f'https://www.cbr-xml-daily.ru/archive/{start_date}/{end_date}/daily.json.js'
    get_exchange_rate_for_currency(url, 'EUR')

    # Добавляем ссылку на git-репозиторий в файл dataset.csv
    add_github_link('dataset.csv')

    # Добавляем ссылку на GitHub в код
    add_github_link('get_exchange_rate.py')

    # Открываем ссылку на репозиторий в браузере
    open_link('https://github.com/bard/get_exchange_rate')

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
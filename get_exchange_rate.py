def get_exchange_rate_for_currency(url, currency):
    # Получаем курс валюты
    rate = get_exchange_rate(url)

    # Сохраняем курс валюты в выходной файл
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    save_exchange_rate(rate, date)
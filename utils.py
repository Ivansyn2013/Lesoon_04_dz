
def currentcy_rates(argv: str):
    '''
    Вывод курса вылют
    :param code: сокращенное отбозначение валюты
    :return: текущий курс к рублю
    '''
    code = argv
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.content.decode(encoding=response.encoding)
    val_name = []
    val_d = dict()
    data_get = content[content.find('Date') + 6:content.find('nam') - 2]

    for el in content.split('<CharCode>', )[1:]:
        char_code = el.split('</CharCode>')[0]
        val_d[char_code] = []
        # val_d[char_code].append((re.split("<Name>|</Name>", el)[1]))

        # Decimal выдает ошибку, атак и не понял почему
        # value_code = Decimal(re.split("<Value>|</Value>", el)[1])

        val_d[char_code].append(re.split("<Value>|</Value>", el)[1])

    if val_d.get(code) != None:
        val = ' '.join(val_d.get(code)).replace(',', '.')
        print(f'{float(val):02.2f}', end=', ')

        data_get = datetime.datetime.strptime(data_get, '%d.%m.%Y')
        print(data_get.strftime('%Y-%M-%d'))
    else:
        print('Неправильно введено значение')


if __name__ == '__main__':
    import requests
    import re
    import datetime
    from decimal import Decimal
    import sys

    currentcy_rates((input('Введи обозначение валюты:')).upper())


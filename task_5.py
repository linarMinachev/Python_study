from sys import argv
from requests import get, utils
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(kzt):
    value = content.split("<Valute ID=")
    d, m, y = map(int, value[0].split('"')[-4].split("."))

    for i in value:
        if kzt.upper() in i:
            print(date(year=y, month=m, day=d), end=", ")
            return float(i.replace("/", "").split("<Value>")[1].replace(",", "."))


if __name__ == "__main__":
    name = argv[1]
    print(currency_rates(name))

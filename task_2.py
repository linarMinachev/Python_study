from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(kzt):
    value = content.split("<Valute ID=")
    for i in value:
        if kzt.upper() in i:
            return float(i.replace("/", "").split("<Value>")[1].replace(",", "."))


rates = (currency_rates("kzt"))
print(f"{rates}")

# Усложнение. Вывести курс за 1 рубль (поделить на <Nominal>)
print()
print("Усложнение задачи. вывести курс за 1 рубль")


def nominal_rates(kzt):
    value = content.split("<Valute ID=")
    for i in value:
        if kzt.upper() in i:
            return int(i.replace("/", "").split("<Nominal>")[1].replace(",", "."))


nominal = nominal_rates("kzt")

result = rates / nominal
print(f"Курс Казахстанских тенге равен: {result} руб.")

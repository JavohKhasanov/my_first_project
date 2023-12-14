import requests

data = requests.get('https://nbu.uz/en/exchange-rates/json/').json()

currency = input("Enter the currency type: ")
currency = currency.upper()
for i in data:
    if i['code'] == currency:
        a = i['cb_price']
        a = float(a)
        print(f'Now the price of the "{currency}" is : {a}')

choise = input("Do you want to calculate the currency to the amount? Enter Yes/No : ")
choise = choise.lower()

if choise == 'yes':
    n = (int(input("Enter a value of currency:  ")))
    if i['code'] == currency:
        a = i['cb_price']
    a = float(a)
    print(f'{n} {currency} is converted to som : {a * n}')
if choise == 'no':
    print("Thank you for using our service")
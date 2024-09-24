currencies = ('USD','EUR','GHC')

exchange_rates =  {
'USD': {'EUR' : 1.5, 'GHC' : 17.8},
'EUR': {'USD' : 0.98, 'GHC' : 19.8},
'GHC': {'EUR' : 0.01, 'USD' : 0.02}
}

while True:
    try:
        amount = float(input('Enter a amount: '))
        if amount <= 0:
            raise ValueError()
        else :
            break
    except ValueError:
        print('Enter a valid amount')


while True:
    source_currency = input('Source currency (USD/EUR/GHC): ').upper() 

    if source_currency not in currencies:
        print('Invalid Currency')
    else:
        break

while True:
    target_currency = input('Source currency (USD/EUR/GHC): ').upper()

    if target_currency not in currencies:
        print('Invalid Currency')
    else:
        break

converted_amount = amount * exchange_rates[source_currency][target_currency]

print(f'{amount} {source_currency} is {converted_amount}{target_currency}')
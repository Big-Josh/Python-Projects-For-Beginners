def get_amount():
    while True:
        try:
            amount = float(input('Enter a amount: '))
            if amount <= 0:
                raise ValueError()
            else :
                return amount
        except ValueError:
            print('Enter a valid amount')


def get_currnecy(label):
    currencies = ('USD','EUR','GHC')
    while True:
        try:
            currency = input(f'{label} currency (USD/EUR/GHC): ').upper() 
            if currency not in currencies:
                print('Invalid Currency')
            else:
                return currency
        except:
            print('Invalid Currency')

def convert(amount,source_currency, target_currency):
    exchange_rates =  {
    'USD': {'EUR' : 1.5, 'GHC' : 17.8},
    'EUR': {'USD' : 0.98, 'GHC' : 19.8},
    'GHC': {'EUR' : 0.01, 'USD' : 0.02}
    }
    if source_currency == target_currency:
        return amount
    else:
        return amount * exchange_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currnecy('Source')
    target_currency = get_currnecy('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is {converted_amount}{target_currency}')

if __name__ == '__main__':
    main()
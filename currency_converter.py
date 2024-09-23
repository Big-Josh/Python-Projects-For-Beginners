

try:
    amount = int(input('Enter a amount: '))
    if amount > 0:
        source_currency = input('Source Currency USD/EUR/GHC').uppeer()
    else :
        print('Enter a valid amount')
except:
    print('Enter a valid amount')
prices = [57.8, 46.51, 97, 11, 14.0, 14.00, 53.09]

for i in prices:
    rub, kop = str(f'{i:.2f}').split(".")
    print(f'{rub} рублей {int(kop):02d} копеек', end=', ')

print('\n')


print(f'ID base: {id(prices)} - {prices}')
prices.sort()
print(f'ID change: {id(prices)} - {prices}')

print('\n')

res = sorted(prices)[::-1]
print(res)
print(f'ID: {id(res)}')

print('\n')

print(res[:5][::-1])

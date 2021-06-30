proceeds = int(input('Введите значение выручки:'))
costs = int(input('Введите значение издержек:'))

profit = proceeds - costs

if proceeds > costs:
    print('Ваша фирма работала с рентабельностью ' + str(round(profit / proceeds, 2) * 100) + '%')
    workers_amount = int(input('Введите кол-во сотрудников:'))
    print('Прибыль фирмы в расчете на одного сотрудника:', profit // workers_amount, 'денежных едениц')
elif proceeds == costs:
    print('Ваша фирма не получила прибыль')
else:
    print('Ваша фирма ушла в убыток')

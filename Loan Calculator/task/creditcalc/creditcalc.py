import math

cal = input('''
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: 
''')

if cal == 'n':
    p = float(input('Enter the loan principal: '))
    m_p = int(input('Enter the monthly payment: '))
    l_i = float(input('Enter the loan interest: '))
    n_i_r = l_i / (12 * 100)
    n_m = math.log((m_p / (m_p - (n_i_r * p))), 1 + n_i_r)
    if n_m / 12 != 1:
        x = divmod(math.ceil(n_m), 12)
        print('It will take {} years and {} months to repay this loan!'.format(x[0], x[1]))
    else:
        print(f'It will take 1 year to repay this loan!')
elif cal == 'a':
    p = float(input('Enter the loan principal: '))
    n_p = int(input('Enter the number of periods: '))
    l_i = float(input('Enter the loan interest: '))
    i = l_i / (12 * 100)
    a = p * (i * math.pow(1 + i, n_p)) / (math.pow(1 + i, n_p) - 1)
    print(f'Your monthly payment = {math.ceil(a)}!')
elif cal == 'p':
    a = float(input('Enter the annuity payment: '))
    n_p = int(input('Enter the number of periods: '))
    l_i = float(input('Enter the loan interest: '))
    i = l_i / (12 * 100)
    p = a / ((i * math.pow((1 + i), n_p)) / (math.pow((1 + i), n_p) - 1))
    print(f'Your loan principal = {round(p)}!')

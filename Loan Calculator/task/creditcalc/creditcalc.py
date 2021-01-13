import math

loan_principal = int(input('Enter your loan principal: '))
calculate = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
""")

a = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
n = math.log(1 + i)(a / a - (i * p))

# if calculate == 'n':
#     monthly_payment = int(input("Enter the monthly payment: "))
#     payment = loan_principal / monthly_payment
#     if payment > 1:
#         print(f"It will take {round(payment)} months to repay the loan")
#     else:
#         print(f"It will take {int(payment)} month to repay the loan")
# elif calculate == 'p':
#     period = int(input("Enter the number of months: "))
#     period_payment = math.ceil(loan_principal / period)
#     last_payment = loan_principal - ((period - 1) * period_payment)
#     if period >= 10:
#         print("Your monthly payment = {}".format(round(period_payment)))
#     else:
#         print(f"Your monthly payment = {period_payment} and the last payment = {last_payment}")

if calculate == 'a':

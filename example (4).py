


income = float(input("Enter your monthly income (Birr):"))


if income <= 2000:
    tax = 0
elif income <= 4000:
    tax = 0.15 * (income)
elif income <= 7000:
    tax = 0.20 * (income)
elif income <= 10000:
    tax = 0.25 * (income)
elif income <= 14000:
    tax = 0.30 * (income)
else:
    tax = 0.35 * (income)


print(f"Your total tax is: {tax} Birr")
print(f"Your net income after tax is: {income - tax} Birr")

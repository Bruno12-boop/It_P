choice = int(input("Enter 1 to calculate Celsius to Fahrenheit, or 2 to change meters to feet: "))

value = float(input("Enter your value: "))

if choice == 1:
    result = value * 1.8 + 32
    print(f"Your calculated result is: {result} °F")

elif choice == 2:
    result = value * 3.28
    print(f"Your calculated result is: {result} feet")
else:
    print("Invalid.")
:
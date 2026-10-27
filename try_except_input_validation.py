try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input: enter a whole number")
else:
    print("You entered:", number)

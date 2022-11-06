def convert_temperature():
    print("\nWhich conversion do you want to choose :- ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice :- "))
    if choice == 1:
        temp = float(input("Enter temperature in celsius :- "))
        print(f"{temp} degree celsius is equal to {(temp*9/5)+32} degree fahrenheit.")
    elif choice == 2:
        temp = float(input("Enter temperature in fahrenheit :- "))
        print(f"{temp} degree fahrenheit is equal to {(temp-32)*5/9} degree clesius")
    else:
        print("Invalid input...please try again\n")

def convert_currency():
    print("\nWhich conversion do you want to choose :- ")
    print("1. Dollar to pound")
    print("2. Pound to Dollar")
    choice = int(input("Enter your choice :- "))
    if choice == 1:
        value = float(input("Enter currency in dollars :- "))
        print(f"{value} dollars in pounds will be {value*0.73}\n")
    elif choice == 2:
        value = float("Enter currency in pounds :- ")
        print(f"{value} pounds in dollar will be {value/0.73}\n")
    else:
        print("Invalid input...please try again")

def convert_length():
    print("\nWhich conversion do you want to choose :- ")
    print("1. Centimeters to foot and inches : ")
    print("2. Foot and inches to Centimeters : ")
    choice = int(input("Enter your choice :- "))
    if choice == 1:
        value = float("Enter length in centimeters :- ")
        inches = value/2.54
        feet = inches / 12
        print(f"{value} centimeters in equal to {feet} feet and {inches} inch\n")
    elif choice == 2:
        feet = float(input("Enter length in feet :- "))
        inches = float(input("Enter length in inches :- "))
        length = (feet*12 + inches)*2.54
        print(f"{feet} feet and {inches} inches in centimeters will be {length}\n")
    else:
        print("Invalid input...please try again")

print("==== Welcome to Value converter =====")
while 1:
    print("\nWhich option would you like to choose :- ")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert Length")
    print("4. Exit")
    choice = int(input("Enter your choice :- "))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_currency()
    elif choice == 3:
        convert_length()
    elif choice == 4:
        print("Exiting....")
        exit(0)

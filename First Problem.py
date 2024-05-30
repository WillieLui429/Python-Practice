def meters_to_km():
    meter = float(input("Enter the number of meters you want to convert to kilometers: "))
    kilo = meter/1000
    print(str(meter) + " meters equals " + str(kilo) + " Kilometers")


def meters_to_inches():
    meter = float(input("Enter the number of meters you want to convert to inches: "))
    inches = meter * 39.37
    print(str(meter) + " meters equals " + str(inches) + " inches")

def meters_to_feet():
    meter = float(input("Enter the number of meters you want to convert to feet: "))
    feet = meter * 3.281
    print(str(meter) + " meters equals " + str(feet) + " feet")

menu = False
while menu != True:
    print("Choose one of the following options: ")
    print("1) Convert to kilometers ")
    print("2) Convert to inches ")
    print("3) Convert to feet ")
    print("4) Quit the program ")
    choice = int(input())
    if choice == 1:
        meters_to_km()

    elif choice == 2:
        meters_to_feet()

    elif choice == 3:
        meters_to_feet()

    elif choice == 4:
        break

    else:
        print("Error try again")

print("Thank you come again")
print("Welcome to the Leap Year Calculator! \n")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year. ")
    elif year % 100 == 0:
        print("Not leap year. ")
    else:
        print("Leap year. ")
else:
    print("Not leap year. ")
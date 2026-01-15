flag_option = False
while flag_option == False:
    print("Choose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter either 1 or 2.")
    else:
        choice = int(choice)
        flag_option = True

flag_temp = False
while flag_temp == False:
    y = input("What is the number you want to convert?")
    if y.replace(".", "").replace(",", "").lstrip('+-').isdigit() == False:
        print("Invalid input. Please enter a numerical value.")
    else:
        y = float(y)
        flag_temp = True

if choice == 1:
    y = (y-32)*5/9
    print(y)
else:
    y = y*9/5+32
    print(y)
#This is a test

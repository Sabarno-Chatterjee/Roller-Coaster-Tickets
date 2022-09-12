print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Please enter your age"))
    if age < 12:
        print("You have to pay $5.")
    elif age < 18:
        print("You have to pay $7")
    else:
        print("You have to pay $15. ")
else:
    print("You cannot ride the roller coaster")

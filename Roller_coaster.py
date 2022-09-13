print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Please enter your age"))
    bill = 0
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 15
        print("Adult tickets are $15. ")
    pic = input("Do you want a photo taken? Enter Y for Yes and N for No.")
    if pic == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
    print(f"Your final bill is {bill}")
else:
    print("You cannot ride the roller coaster")

print("Welcome to the roller coaster")
height = int(input("What is your height? "))


if height >120:
    print("You can acess the ride")
    age = int(input("What is your age? "))
    if age >= 12 >= 18:
        print("Your price is 7$")
    elif age < 12:
        print("Your price is 5$")
    else:
        print("Your price is 12$")
else:
    print("Sorry but you cant access the ride")


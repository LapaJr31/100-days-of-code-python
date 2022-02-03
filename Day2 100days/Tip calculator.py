print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip_percentage = input("What percentage of tip you want to give? ")
people_spilt = input("How many people to spilt the bill? ")

bill2 = float(bill)
tip_percentage2 = float(tip_percentage)
people_spilt2 = float(people_spilt)

tip_perc_number =  tip_percentage2 / 100
tip_per_person = round((bill2 / people_spilt2) * tip_perc_number , 2)
price_per_person = round(bill2 / people_spilt2 , 2)
finish_price = tip_per_person + price_per_person

print(f"Each person should pay {finish_price}, which consists from {price_per_person} - total price, {tip_per_person} - tip from every person")
print("Have a nice day!")




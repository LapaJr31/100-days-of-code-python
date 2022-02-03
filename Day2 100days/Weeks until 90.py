age = input("Tell me your age in years\n")

weeks_in_90_years = 4680
weeks_in_one_year = 52

weeks_in_90_years1 = int(weeks_in_90_years)
weeks_in_one_year1 = int(weeks_in_one_year)
age1 = float(age)

life_liven = age1 * weeks_in_one_year1
life_left_until_90_years = weeks_in_90_years1 - life_liven
print(f"You have {life_left_until_90_years} weeks left until 90 years")
from datetime import date

birth_year = input("Please enter your birth year: ")
current_year = date.today().year

age = current_year - int(birth_year)

print(age)
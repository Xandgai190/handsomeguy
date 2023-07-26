from datetime import date
today = date.today()

birthYear = int(input("Your BirthYear?"))
age = today.year - birthYear

if 15 <= age <=20:
    print("teenager")

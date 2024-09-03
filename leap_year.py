def leap_year():
    year=int(input("Ingrese un year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100):
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")

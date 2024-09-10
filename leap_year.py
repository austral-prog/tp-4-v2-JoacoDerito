def leap_year():
    y = int(input("Ingrese un año: "))

    d4 = not y % 4      # Es divisible por 4?
    d100 = not y % 100  # Es divisible por 100?
    d400 = not y % 400  # Es divisible por 400?

    # Si es div. por 4 pero no centenario ó div. por 400
    if (d4 and not d100) or d400:
        print(f"El año {y} es bisiesto")
    else:
        print(f"El año {y} no es bisiesto")

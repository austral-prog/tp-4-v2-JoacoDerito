def line():
    import math
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el valor de X1: "))
    x2 = float(input("Ingrese el valor de X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El valor de X1 es: {x1}")
    print(f"El valor de X2 es: {x2}")
    y1 = a * x1 + b
    y2 = a * x2 + b
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"La distancia entre ellos es: {distance}")

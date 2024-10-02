import math
cathetus_1 = float(input("Введите длину первого катета: "))
cathetus_2 = float(input("Введите длину второго катета: "))

hypotenuse = math.sqrt(cathetus_1**2 + cathetus_2**2)  
area = hypotenuse / 2
print(f"Площадь треугольника равна {area:.2f}")
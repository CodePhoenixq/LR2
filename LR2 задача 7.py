import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите радиус круга: "))

T = math.sqrt(x**2 + y**2) > r

print(f"Точка ({x}, {y}) лежит вне круга: {T}")




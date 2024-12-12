k = 15

# Вычисляем k mod 7 (остаток от деления k на 7)
k_mod_7 = k % 7

# Вычисляем k div 5 (целочисленное деление k на 5)
k_div_5 = k // 5

# Вычисляем k div 5 - 1
result = k_div_5 - 1

# Проверяем, выполняется ли равенство
if k_mod_7 == result:
    print(f"Утверждение k mod 7 = k div 5 - 1 верно для k = {k}")
    print(f"k mod 7 = {k_mod_7}")
    print(f"k div 5 - 1 = {result}")
else:
    print(f"Утверждение k mod 7 = k div 5 - 1 неверно для k = {k}")
    print(f"k mod 7 = {k_mod_7}")
    print(f"k div 5 - 1 = {result}")


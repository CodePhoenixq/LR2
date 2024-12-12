p = True
q = True

# Вычисляем (p < True)
result1 = (p < True)  # Булево сравнение: True < True -> False

# Вычисляем (q = False)
result2 = (q == False) # Булево сравнение: True == False -> False

# Сравниваем результаты
final_result = (result1 == result2)

print(f"Результат (p < True) = {result1}")
print(f"Результат (q == False) = {result2}")
print(f"Результат ((p < True) == (q == False)) = {final_result}")


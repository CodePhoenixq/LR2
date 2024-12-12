def convert_to_meters(unit_number, length):
 
    if not 1 <= unit_number <= 5:
        return None

    if unit_number == 1:  # Дециметр
        return length * 0.1
    elif unit_number == 2:  # Километр
        return length * 1000
    elif unit_number == 3:  # Метр
        return length
    elif unit_number == 4:  # Миллиметр
        return length * 0.001
    elif unit_number == 5:  # Сантиметр
        return length * 0.01


# Пример использования
unit_number = int(input("Введите номер единицы измерения (1-5): "))
length = float(input("Введите длину отрезка: "))

meters = convert_to_meters(unit_number, length)

if meters is not None:
    print(f"Длина отрезка в метрах: {meters}")
else:
    print("Некорректный номер единицы измерения.")


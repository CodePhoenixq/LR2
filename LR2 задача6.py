def is_strictly_increasing(n):
    
    if not 1000 <= n <= 9999:
        return False

    s_n = str(n)
    for i in range(len(s_n) - 1):
        if int(s_n[i]) >= int(s_n[i+1]):
            return False
    return True


# Пример использования
n1 = 1234
n2 = 1223
n3 = 9876
n4 = 1000
n5 = 1235
n6 = 1111

print(f"Число {n1}: {is_strictly_increasing(n1)}")  # True
print(f"Число {n2}: {is_strictly_increasing(n2)}")  # False
print(f"Число {n3}: {is_strictly_increasing(n3)}")  # False
print(f"Число {n4}: {is_strictly_increasing(n4)}")  # False
print(f"Число {n5}: {is_strictly_increasing(n5)}")  #True
print(f"Число {n6}: {is_strictly_increasing(n6)}")  # False


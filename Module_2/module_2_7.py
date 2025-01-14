def generate_password(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число (от 3 до 20): "))

if 3 <= n <= 20:
    result = generate_password(n)
    print(f"Нужный пароль для {n}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")
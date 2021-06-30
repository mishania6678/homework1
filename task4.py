num = int(input('Введите число:'))

# Оптимальное решение:
# print(int(max(str(num))))

max_digit = num % 10
while num != 0:
    if max_digit < num % 10:
        max_digit = num % 10
    num //= 10

print(max_digit)

# test1

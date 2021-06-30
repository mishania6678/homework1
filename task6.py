a = int(input('Введите ппреодоленное за первый день расстояние:'))
b = int(input('Введите целевой результат:'))

counter = 1
distance = a
while distance < b:
    distance *= 1.1
    counter += 1

print(counter)

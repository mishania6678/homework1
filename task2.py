time_in_seconds = int(input('Введите время в секундах:'))
hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours * 3600) // 60
seconds = time_in_seconds - hours * 3600 - minutes * 60
print(f'{hours}:{minutes}:{seconds}')

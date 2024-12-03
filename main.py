
hour = int(input('Введите часы: '))
minute = int(input('Введите минуты: '))
difference = int(input('Введите разницу: '))

new_hour = hour + difference

if new_hour > 24:
    new_hour -= 24
if new_hour < 0:
    new_hour += 24
print(f'{new_hour}:{minute}')



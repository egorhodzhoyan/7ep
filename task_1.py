result = 0
for number in -6, 11, 4, 10, 54, 67, 6, 211, 200, 555:
    if  number > 0 and number % 2 == 0:
        result += 1
print('Количество корректных номеров (чётных и положительных):', result)
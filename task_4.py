summ = 0
count = 0
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print('Числа из отрезка, которые делятся на 3:')
for i in range(a, b + 1):
    if i % 3 == 0:
        print(i)
        summ += i
        count += 1
print('Среднее арифметическое: ', summ / count)
a = int(input('Введите первое двузначное число: '))
b = int(input('Введите второе двузначное число: '))
print('Замечательные числа в диапазоне двузначных:')
for number in range (a, b + 1) :
    perfect_number = ((number % 10) * (number // 10) )* 3
    if number == perfect_number:
        print(number)
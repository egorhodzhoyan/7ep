three = 0
four = 0
five = 0
students = int(input('Сколько в классе учеников? '))
for student in range(1, students + 1):
    grade = int(input('Введите оценку ученика: ')) # Оценки только - 3, 4, 5!
    if grade == 3:
        three += 1
        #print(three)
    elif grade == 4:
        four += 1
        #print(four)
    else:
        five += 1
        #print(five)
if three > four and three > five:
    print('Сегодня больше троешников!')
elif four > three and four > five:
    print('Сегодня больше хорошистов!')
elif five > three and five > four:
    print('Сегодня больше отличников!')
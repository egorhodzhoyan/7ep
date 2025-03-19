average_salary = 0
salary_year = 0
for months in range(12):
    salary_month = int(input('Введите зарплату сотрудника за месяц: '))
    salary_year += salary_month
    average_salary = salary_year / 12
print('Средняя зарплата за год:', average_salary)
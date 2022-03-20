# Количество дней
# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
#
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
#
# Примечание 2. Считайте, что год является невисокосным.
#
# Примечание 3. Следующий программный код:
#
# print(get_days(1))
# print(get_days(2))
# print(get_days(9))
# должен выводить:
#
# 31
# 28
# 30

def get_days(month):
    thirty = [4, 6, 9, 11]
    if month == 2:
        return 28
    elif month in thirty:
        return 30
    else:
        return 31

# def get_days(month):
#     m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return m[month - 1]

# return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

num = int(input())
print(get_days(num))
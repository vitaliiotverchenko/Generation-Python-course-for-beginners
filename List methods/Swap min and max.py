# Переставить min и max
# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести строку текста в соответствии с условием задачи.
#
# Примечание. Используйте подходящие встроенные функции и списочные методы

str_of_num = input().split()
for i in range(len(str_of_num)):
    str_of_num[i] = int(str_of_num[i])
max_index = str_of_num.index(max(str_of_num))
min_index = str_of_num.index(min(str_of_num))
str_of_num[min_index], str_of_num[max_index] = str_of_num[max_index], str_of_num[min_index]
print(*str_of_num)
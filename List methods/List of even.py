# На вход программе подается четное число n, \, n \ge 2n,n≥2. Напишите программу, которая выводит список четных чисел
#
#  [2, 4, 6, ..., n].
#
# Формат входных данных
# На вход программе подается четное натуральное число.
# 
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
print([i for i in range(2, n+2, 2)])

#print(list(range(2, int(input()) + 1, 2)))

#print([i for i in range(2, int(input())+1, 2)])
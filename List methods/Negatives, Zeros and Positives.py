#Negatives, Zeros and Positives
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
negative = []
null = []
positive = []
for i in range(n):
    a = int(input())
    if a <0:
        negative.append(a)
    elif a == 0:
        null.append(a)
    elif a > 0 :
        positive.append(a)
negative.extend(null)
negative.extend(positive)
print(*negative, sep='\n')
# На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
#
# Формат входных данных
# На вход программе подается натуральное число nn, а затем nn строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 1 2 3 4
# 5 6 7
# 10 11 17
# Sample Output 1:
#
# 1 2 3 4 5 6 7 10 11 17
# Sample Input 2:
#
# 4
# 10 20
# 1 15
# 5 17
# 8 13 19
# Sample Output 2:
#
# 1 5 8 10 13 15 17 19 20

def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):  # пока не закончится хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):  # прицепление остатка
        result += list2[p2:]
    return result


n = int(input())
total_list = []
for i in range(n):
    num = [int(q) for q in input().split()]
    total_list = quick_merge(total_list, num)

print(*total_list)


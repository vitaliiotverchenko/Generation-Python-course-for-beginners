# #Второе вхождение
# На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

s = input()
count = s.count('f')
if count == 0:
    print(-2)
elif count == 1:
    print(-1)
else:
    s = s.replace('f', '4', 1)
    print(s.find('f'))
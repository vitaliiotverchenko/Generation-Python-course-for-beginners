# Корректный ip-адрес
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
#
# Формат выходных данных
# Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
#
# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.

# ip_address = input().split('.')
# answer = True
# for i in range(len(ip_address)):
#     ip_address[i] = int(ip_address[i])
#     if 0 > ip_address[i] or ip_address[i] > 255:
#         print('НЕТ')
#         answer = False
#         break
# if answer:
#     print('ДА')

ip_address = input().split('.')
answer = True
for i in ip_address:
    if 0 > int(i) or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')

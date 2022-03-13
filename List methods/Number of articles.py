# Количество артиклей
# На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
#
# Формат входных данных
# На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.
#
# Формат выходных данных
# Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.
#
# Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'

text = input().split()
articles = ['a', 'A', 'an', 'An', 'the', 'The']
count = 0
for i in range(len(articles)):
    count += text.count(articles[i])
print('Общее количество артиклей:', count)

# s = input().split()
# print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")

# sp = input().lower().split()
# a = sp.count("a") + sp.count("an") + sp.count("the")
# print("Общее количество артиклей:", a)
a1, b1, a2, b2 = int(input('')), int(input('')), int(input('')), int(input(''))
if a1 != b1 != a2 != b2:
    if a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
        print('пустое множество')
    elif a1 < a2 < b1 < b2:
        print(a2, b1)
elif a2 < a1 < b2 < b1 or (a1 == a2) < b2 < b1 or a2 < (a1 == b2) < b1:
    print(a1, b2)
elif a2 < a1 < b1 < b2 and b1 != a2 != a1:
    print(a1, b1)
elif a1 < (b1 == a2) < b2:
    print(b1, a2)
elif a1 < a2 < b2 < b1 or a1 < a2 < (b1 == b2):
    print(a2, b2)
elif (a1 == a2) < b1 < b2 or a2 < a1 < (b1 == b2) or (a1 == a2) < (b1 == b2):
    print(a1, b1)

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def e(text, rotation): #функция отвечает за шифровку
    text = text.upper()  # в капс (верхний регистр))
    newtext = ""


    # цикл перебирает строку посимвольно
    for c in text:

        if ( a.find(c) == -1 ): #отвечает за поиск буквы в альфавите 
            newtext += c

        else:
            pos = a.find(c) # S - 18   pos = 18
            pos += rotation # 18 + 9   pos = 27

            # Если искать позицию через минус
            #  27 - len(a)  27 - 26 = 1 - для маленькой ротации работает
            # 19 + 100   pos = 119 - для большой ротации НЕТ
            # 119 - len(a) = 95 - ERROR

            pos = pos % len(a)  # 27 % 26 = 1
                                # 119 % 26 = 15
                                # 24 % 26 = 24

            new_letter = a[ pos ]  # new_letter = a[1]  (a[1] = B)
            newtext += new_letter

            #newtext += (a[(a.find(c) + rotation) % len(a)])



    return newtext

# S C H O O L    9
# B L Q X X U


def d(text, rotation): #функция отвечает за дешифровку
    text = text.upper()
    newtext = ""
    for c in text:
        if (a.find(c) == -1):
            newtext += c
        else:

            pos = a.find(c)     # B - 1   pos = 1
            pos -= rotation     # 1 - 9   pos = -8
            pos = pos % len(a)  # -8 % 26  = -8
            new_letter = a[pos] # new_letter = a[pos] (a[-8] = S)
                                # Отрицательный индекс берет букву с конца (8 буква с конца - S)
            newtext += new_letter

            #newtext += (a[(a.find(c) - rotation) % len(a)])


    return newtext




w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1: #первый мод отвечает за шифрование
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Encrypted: " + e(text, rotation))
elif mode == 2: #второй мод отвечает за дешифрование
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Decrypted: " + d(text, rotation))
elif mode == 3: #третий мод не делает ничего, просто  
    print("Bruteforcing...")
    print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
    text = input("Enter the text: ")
    for i in range(1,26):
        print("Decrypted: " + d(text, i))


# Алгоритм Винежера - шифр смещение
# Шифруемая строка - school
# Ключ шифрования - key
# S - 19   K - 11    19 + 11 = 30 % 26 = 4 -> D
# C - 3    E - 5     3  + 5  = 8 -> H
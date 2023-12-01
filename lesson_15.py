# Работа с фалйами
# Файл может содержать текстовую информацию .txt .py  .c  .cpp  .ini  .bat  .html  .css
# Файл может содержать байтовую информацию - набор байтов в файле
#
# Для работы с фалйами необходимо открыть поток ( открыть файл )
#   За открытие потока отвечает функция open(), возвращает объект потока
#   И уже из этого потока можно читать или писать
#   После окончания работы с файлом - поток нужно закрыть  .close()

#  open( "путь/до/файла", "режим_открытия", enconding="кодировка" )
#  Режимы открытия файлов
#       r  - чтение
#       w  - запись (перезапись). Если файла нет, файл создается
#       a  - дозапись (пополнение). Если файла нет, он создастся
#       x  - создать эклюзивный файл, если файл уже существует - вызывает ошибку
#       +  - открыть файл и в режиме чтения и записи одновременно

file = open( 'lesson_15.txt', 'r', encoding='utf-8' )

# Чтение
# .read() - считывает полночтью весь файл как одну строку
# .read(n) - считать следующие n символов из файла
# .readline() - считывает символы до первого найденного символа /n
# .realines() - считывает все строки, и возвращает результат в виде списка

#text = file.read()

#text = file.read(10)

#text = file.readline()

text = file.readlines()
print( text, len(text) )


file.close()  # применили к объекту потока метод .close() т.е. закрыли

# Запись
file = open( 'lesson_15_w.txt', 'w', encoding='utf-8')

# .write( строка ) - пишет в файл переданную строку
# . writelines( список ) - пишет в файл переданный список строк

text = 'Bye from Python'
text_list = [ 'Hello\n', 'From\n', 'Python\n' ]
#file.write( text )

file.writelines( text_list )

file.close()


# Дозапись - функции такие же как у обычной записи (w), но в файле остается
#  старая информация
file = open( 'lesson_15_w.txt', 'a', encoding='utf-8')
text = 'Bye from Python'
text_list = [ 'Hello\n', 'From\n', 'Python' ]

file.write(text)

file.close()


# Ключ слово with - позволяет писать меньше кода, а так же открывать за один раз
#   несколько файлов

file = open( 'lesson_15.txt', 'r', encoding='utf-8' )
text = file.read()
file.close()

with open( 'lesson_15.txt', 'r', encoding='utf-8' ) as file:
    text = file.read()

# Можем открыть несколько файлов за раз
with open('lesson_15.txt') as file1 ,  open('lesson_15_w.txt') as file2:
    text1 = file1.read()
    text2 = file2.read()


# Работа со строками str
# Строки заключаются любо в одиночные либо в двойные кавычки (нельзя в две разные)
#* "Hello" - GOOD
#* 'Hello' - GOOD
#! "Hello' - BAD

# Строка может содержать внутри кавычки другого типа
# 'Мы "Викинги", народ севера!'
# " I'm 15 years old "

# Что если нужно использовать в самом тексте, кавычки такого же типа
# "Мы "Викинги", народ севера!" - ERROR
# "Мы \"Викинги\", народ севера!"
# - Символ "\" - экранирует (защищает) символы в строке
# Что бы в строке был обратный слеш, его самого нужно экранировать \\
print( 'Hehe \\nene' )


# Строка НЕИЗМЕНЯЕМЫЙ объект, все манипуляции со строками - создают измененную КОПИЮ
# Со строкой можно работать как с списком (срезы, образение к элементам по индексу)
text = 'Hello World'
print( text[0] ) # один символ
print( text[2:6] ) #срез
print( text[:6:2] )
print( text[::-1] )

# Строку можно перебирать циклом for
text = 'Hello World'
for s in text:
    print( s )


# .replace( old, new )
# .index( text )
# .find( text )
# .split( delimiter )
# .join(list)
# .lower()
# .upper()
# .capitalize()

text = "Hello World"
newtext = text.replace( 'World', 'Python' )  # заменить в строке World на Python
print( text )
print( newtext )

# Результат сохраняем в переменную, т.к. создалась измененная копия, оригинал остался старым

# ------------------------------
# 05.06.2023
# ------------------------------
nums = [1,2,3,4,5]
nums[0] = 0
print( nums )

text = "Hello World"
#text[0] = 'L'  # НЕЛЬЗЯ

# .index( text ) 
# .find( text )
text = "Hello World"
res = text.find( "wo" )
print( res )
# Обе функции возвращают индекс начала искомой строки. Если не нашло
#   index() - Error
#   find() -  -1


# .lower() - в верхний регистр
# .upper() - в нижний регистр
# .capitalize() - первая буква большая, остальные маленькие
text = 'HeLlo WOrlD'
newtext = text.lower()
print( newtext ) # hello world

newtext = text.upper()
print( newtext ) # HELLO WORLD

newtext = text.capitalize()
print( newtext ) # Hello world


# .split( delimiter ) - разбивает строку на список, по указанному разделителю
# str.join(list) - из списка создает строку, где элементы отделены str разделителем (строка)
text = 'Big lazy fox jumps over the fence'
words = text.split( ' ' )
print( words )

text = "aaaaaaaaaaaaaaaaaaaXXXbbbbbbbbbbbbbbbb"
parts = text.split('XXX')
print( parts )

words = ['Big', 'lazy', 'fox', 'jumps', 'over', 'the', 'fence']
res_text = "_".join( words )
print( res_text )

# Задание
symbols = "!(){}[].,?:;-\"'"
text = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
# Убрать из текста, все перечисленные в переменной "symbols" символы

#newtext = newtext.replace( '!', '' )
#newtext = newtext.replace( '(', '' )
#newtext = newtext.replace( ')', '' )
#newtext = newtext.replace( '{', '' )

newtext = text
for s in symbols:
    newtext = newtext.replace( s, "" ) 

print( newtext )
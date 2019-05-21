# print ('Hello world')
# a, b, c = 1, 1, 43
# print (a, b, c)

# var = 3.14
# print (var)
# var = 'ko ko ko'
# print (var)
# var = True
# print (var)

# user = input('I am a Python, and what is your name?:')
# print ( 'Weclome,', user )

# lang = input('what is your favorite programming langiage?:')
# print (lang, 'Is', 'fun', sep = ' * ', end= '!\n') #  sep = ' * ' - указание разделителя, end= '!\n'  - конец строки с переносом

# number = 3
# print ((number + 3) * 8)

# + # сложние
# - # вычитание
# * # умножение
# / # деление
# % # деление по модулю
# // # цельночисловое деление
# ** # возведение в степень
#print (1532512 % 23)# Оператор % (деление по модулю) делит одно число на другое и возвра- щает остаток от деления.
# print ( 25 // 12)
# print ( 25 / 12)
# print (25 ** 2)

# a = 7
# b = 3
#
# print ('Slojenie:\t', a, '+', b, '=', a + b) #\t— это так называемая управляющая последова- тельность, которая добав- ляет невидимый символ табуляции для форматирова- ния вывода.
# print ('Ryznitsa:\t', a, '-', b, '=', a - b)
# print ('Ymnojenie:\t', a, 'x', b, '=', a * b )
# print ('Delenie:\t', a, ':', b, '=', a / b)
# print ('Tseloe delenie:\t', a, '::', b, '=', a // b)
# print ('Ostatok del:\t', a, '%', b, '=', a % b)
# print ('Stepen\':\t', a, '^', b, '=', a ** b)


# Оператор    Пример  Эквивалентная операция
# =           a=b     a=b
# +=          a+=b    a=(a+b)
# -=          a-=b    a=(a—b)
# *=          a*=b    a=(a*b)
# /=          a/=b    a=(a/b)
# %=          a%=b    a=(a%b)
# //=         a//=b   a=(a//b)
# **=         a**=b   a=(a**b)



# a = 7
# b = 3
#
# a += b
# print ('Slojenie:\t\t', 'a = ', a, '(3 + 7)' )
# a -= b
# print ('Vichitanie:\t\t', 'a = ', a, '(10 - 3)')
# a *= b
# print ('Ymnojenie:\t\t', 'a = ', a, '(7 * 3)')
# a /= b
# print ('Delenie:\t\t', 'a = ', a, '(21 / 3)')
# a //= b
# print ('Tseloe delenie:\t\t', 'a = ', a, '(7 // 3)')
# a %= b
# print ('Ostatok del:\t\t', 'a = ', a, '(2 // 3)')
# a **= b
# print ('Stepen\':\t\t', 'a = ', a, '(2 ** 3)')
#
#
# Оператор    Проверяемое условие
# ==          Равенство
# !=          Неравенство
# >           Больше
# <           Меньше
# >=          Больше либо равно
# <=          Меньше либо равно

# nil = 0
# num = 0
# max = 1
# cap = 'A'
# low = 'a'
#
# print ('Equility:\t', nil, '==', num, nil == num)
# print ('Equility:\t', cap, '==', low, cap == low)
# print ('Inequility:\t', nil, '!=', max, nil != max)
# print ('Greater:\t', nil, '>', max, nil > max)
# print ('Lesser:\t', nil, '<', max, nil < max)
# print ('More ot equal:\t', nil, '>=', num, nil >= num)
# print ('Less ot equal:\t', max, '<=', num, max <= num)
#
#
# Оператор    Операция
# and         Логическое «И»
# or          Логическое «ИЛИ»
# not         Логическое «НЕ»
# a = True
# b = False
#
#
# print ('AND Logic:')
#
# print ('a and a = ', a and a)
# print ('a and b = ', a and b)
# print ('b and b = ', b and b)
#
# print ('\nOR Logic:')
#
# print ('a or a = ', a or a)
# print ('b or a = ', b or a)
# print ('b or b = ', b or b)
#
# print ('\nNOT Logic')
# print ('a = ', a, '\tnot a = ', not a)
# print ('b = ', b, '\tbot b = ', not b)



# a = 1
# b = 2
#
# print ('\nVariable a is:', 'One' if (a == 1) else 'Not one')
# print ('Variable a is:', 'Even' if (a % 2 == 0) else 'Odd')
#
# print ('\nVariable b is:', 'One' if (b == 1) else 'Not one')
# print ('Variable b is:', 'Even' if (b % 2 == 0) else 'Odd')
#
# max = a if (a > b) else b
#
# print ('\nGreather valuse is:', max)



# В таблице ниже перечисляются операторы в порядке убывания приоритета.
# Те из них, что находятся в строках выше, имеют более высокий приоритет.
# Приоритет операторов, находящихся на одной строке в таблице,
# определяется правилом «слева направо».
#
# Оператор    Описание
# **          Возведение в степень
# +           Положительное значение
# -           Отрицательное значение
# ~           Побитовое отрицание
# *           Умножение
# /           Деление
# //          Целочисленное деление
# %           Деление по модулю
# +           Сложение
# -           Вычитание
# |           Побитовое ИЛИ
# ^           Побитовое исключающее ИЛИ
# &           Побитовое И
# >>          Побитовый сдвиг вправо
# <<          Побитовый сдвиг влево
# >,<=,<,<=,==,!= Сравнение
# =, %=, /=, //=, -=, +=, *=, **= Присваивание
# is, is not  Идентичность
# in, not in  Вхождение
# not         Логическое отрицание
# and         Логическое И
# or          Логическое ИЛИ

# a = 2
# b = 4
# c = 8
#
# print ('\nDefault order:\t', a, '*', c, '+', b, '=', a * c + b)
# print ('Forced order:\t', a, '* (', c, '+', b, ') = ', a * (c + b) )
# print ('\nDafeult order:\t', c, '//', b, '-', a, '=', c // b - a)
# print ('Forced order:\t', c, '// (', b, '-', a, ') =', c // (b - a))
# print ('\nDefault order:\t', c, '%', a, '+', b, '=', c % a + b)
# print ('Forced order:\t', c, '% (', a, '+', b, ') =', c % (a + b))
# print ('\nDefault order:\t', c, '**', a, '+', b, '=', c ** a + b)
# print ('Forced order:\t', c, '** (', a, '+', b, ') =', c ** (a + b))

#строковые (str(string)), целочислен- ные (int(integer)), с плавающей точкой (float(floating-point)) - типы переменных

# Функция     Описание
# int(x)      Преобразует х в целое число
# float( x )  Преобразует х в число с плавающей точкой
# str(x)      Преобразует х в строковое представление
# chr(x)      Преобразует целое х в символ
# unichr( x ) Преобразует целое х в символ Юникода (Unicode)
# ord(x)      Преобразует символ х в соответствующее ему целое число
# hex(x)      Преобразует целое х в шестнадцатеричную строку
# oct(x)      Преобразует целое х в восьмеричную строку
# type(x)     Возвращает тип переменной


# a = input ('Enter a number:')
# b = input ('Enter another one:')
#
# # sum = a + b
# sum = int(a) + int(b)
# sum = chr(int(sum))
# print ('\n Sum data btype:\t', sum, type(sum))
# a = 10
# b = 5
# print ('a =', a, '\tb = ', b)
# a = a ^ b
# print (a)
# b = a ^ b
# print (b)
# a = a ^ b
# print(a)

#СПИСКИ:
# q = ['January', 'February', 'March']
# print ('First month:\t', q[0])
# print ('Second month:\t', q[1])
# print ('Third month:\t', q[2])
#
# c = [[1, 2, 3], [4, 5, 6]]
# print ('\nTop Left: 0,0\t', c[0][0])
# print ('\nBottom Right: 1,2\t', c[1][2])
# print ('\nSeconf month first letter:\t', q[1][0])

#РАБОТА СО СПИСКАМИ
# Метод списка        Описание
# list.append(x)      Добавляет элементхв конец списка
# list.extend(L)      Добавляет все элементы спискаLв конец списка
# list.insert(i,x)    Вставляет элементxв позицию перед индексом iв списке
# list.remove(x)      Удаляет первый элементхиз списка
# list.pop(i)         Удаляет элемент с индексомiи возвращает его
# list.index(x)       Возвращает индекс первого элементахв списке
# list.count(x)       Возвращает количество вхождений элемента x в список
# list.sort()         Сортирует элементы списка по возрастанию
# list.reverse()      Обращает порядок следования элементов

b = ['Apple', 'Bun', 'Cola']
c = ['Egg', 'Fig', 'Grape']
print ('B List:', b)
print ('B length:', len(b))
b.append ('Damson')
print ('\nAppended:', b)
print ('Last intem removed:', b.pop())
print ('B List:', b)
b.extend(c)
print ('Extended:', b)
del b[1]
print ('Removed:', b)
del b[1:3]
print ('Slicely removed:', b)

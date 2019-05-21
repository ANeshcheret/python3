#больше чем
print(2 > 3)
#меньше чем
print(2 < 3)
#больше или равно
print(2 >= 2)
#меньше или равно
print(1 <= 4)
#равно
print(2 == 2)
print(2 == '2')
print('hi' == 'bye')
#не равно
print(2 != 2)
print(1 != '1')

#x in list
print(1 in [1,2,3])
print(4 in [1,2,3])

#x not in lsit

print(4 not in [1,2,3])
print(1 not in [1,2,3])

#and
print((1>2) and (2<3)) #false
#or
print((1>2) or (2<3)) # true
#Not
print(not 2>=1) # false

#кортежи

tuple = ()
t1 = (1,2,3)
print(t1[0])

t2 = (3,) #кортеж из одного элемента

t3 = ('a', True, 123)

str, b, num = t3 # распаковка кортежа, каждая переменная получила элемент кортежа по порядку
print(str)
print(b)
print(num)



####множества


x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(3.14)
print(x)

#убрать повторяющеися элементы
words = ['hello', 'Kostya', 'hello', 'Anna']
set(words)
print(set(words))


#конвертировать список в множество

converted = set([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2])
print(converted)

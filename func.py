def my_func(x, y):
    #pass # функции с пустым телом запрещены
    return x + y

print(my_func(10,10))


def my_func1(a, b):
    return a + b
print(my_func1('hello', ' kostya'))


def my_func2(z, c, my_string='Python'):
    '''
    DOCSTRING
    '''
    print('My first {} function!'.format(my_string))
    return z + c
print(my_func2('hello', ' kostya'))


def func(*args):
    return args
print(func(2,7,'true', True, 'Python'))

print('\n')

l = [1,2,3,4,5,6,7,8]
def even(num):
    return num % 2 == 0

evens = filter(even, l)
print(list(evens))

print('\n')

l = [1,2,3,4,5,6,7,8]
lambda num: num % 2 == 0
evens2 = filter(lambda num: num % 2 == 0, l)
print(list(evens2))

print('\n')

l1 = [12,3,4]
l2 = l1
print(l1, l2, id(l1), id(l2))

l1[2] = 10
print(l1, l2, id(l1), id(l2))


v1 = 1024
v2 = v1
print(v1, v2, id(v1), id(v2))
v1 = 2048
print(v1, v2, id(v1), id(v2))

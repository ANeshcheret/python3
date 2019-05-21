#10 / 0
# print(int('Hello'))
# print([1,2,3] + 'Hello')

try:
    f = open('simple.txt', 'w')
    f.write('test write ti simple test!')
except IOError:
    print('Error: could not find fila or read data')
else:
    print('Success')
    f.close()

try:
    f = open('simple.txt', 'r')
    f.write('test write ti simple test4124324!')
except IOError:
    print('Error: could not find fila or read data')
finally:
    print('I always work')
    f.close()


#raise NameError('Hello Python!')

class MyError(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise MyError(3*3)
except MyError as e:
    print('My Exception with value: ', e.value)

x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())


print('\n')

name = 'This is a global name'

def greet():
    name = 'Lisa'

    def hello():
        print ('Hello ' + name)
    hello()
print (greet())
print(name)

print('\n')

y = 50

def func2():
    y = 100

print('before function call, y is: ', y)
func2()
print('after function call, y is: ', y)
def func3():
    global y
    y = 100
print('before function call, y is: ', y)
func3()
print('after function call, y is: ', y)

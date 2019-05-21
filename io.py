print('Hello')
#
print('Hello' + ' python')
#
print('Python: ' + str(3))
#
print('A', 'B', 'C')
#
print('A', 'B', 'C', sep='#') ##разделитель
#
for i in range(3):
    print('i: ' + str(i)) ## \n
#
for i in range(3):
    print('[i: ' + str(i) + ']',end='--')

print('\n')
print('\n')


# print(input())

# a = input()
# print(a)

#
# val = int(input())
# print(type(val))
# print(val)

# number = int(input('Please input a number: '))
# print('Here is it: ', number)

# l = input().split() # разделитель
# print(l)

# l1 = input().split('-') # разделитель
# print(l1)

nums = map(int, input().split())#В Python функция map принимает два аргумента:
print(list(nums))#функцию и аргумент составного типа данных,
#например, список. map применяет к каждому элементу списка переданную функцию.

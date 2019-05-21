print('task1'.upper(),'\n')

s = 'python'
print(s[0])
print(s[-2])
print(s[0:4])
print(s[1:4])
print(s[-2:])
print(s[::-1])
print(s[::2], '\n')

print('task2'.upper(),'\n')

age = 10
name = 'Lisa'

s = 'Hello my cat\'s name is {n} and she is {n} years old'.format(n = 'Lisa', y = '10')
print(s, '\n')

print('task3'.upper(), '\n')

l = [21, 2, [3,12,True], [10,13, 'Hello', False]]
print(l)
print(l[3][2])
l[3][2] = 'Goodbye'
print(l[3][2])
print(l, '\n')

print('task4'.upper(), '\n')

d1 = {'key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['deep', ['hello']]}]}

print(d1['key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0], '\n')

print('task5'.upper(), '\n')

mylist = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
print(set(mylist))

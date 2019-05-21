mylist = [1,2,3]
mylist1 = []
mylist2 = ['z']

l3 = ['test', 10, True, [1,2,3]]

print(l3)
print(list('Lists'))
print(len(l3))
print(l3[1])

l4 = ['a', 'b', 'c', 'd', 'e']

print(l4[1:3]) # Первый индекс в срезе – начало диапазона (включительно), второй – конец диапазона (исключительно).
print(l4[:3])
l4[0] = 'new item'
print(l4)
l4.append('New element')
print(l4)
l4.append(['x', 'y', 'z'])
print(l4)
l5 = ['x', 'y', 'z']
l4.extend(l5)
print(l4)
l5.pop(1)
print(l5)

l6 = ['q', 'w', 'e']
l6.reverse()
print(l6)

l7 = [10, 1, 5, 11]
l7.sort()
print(l7)

l8 = [1, 2, ['x', 'y', 'z']]
print(l8[2][1])

matrix = [[1,2,3], [4,5,6], [7,8,9]]
# 123
# 456
# 789
second_col = [ex[2] for ex in matrix]
print(second_col)

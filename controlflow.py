###--IF--####
number = int(input('Enter the number:'))

if number > 5:
    print('Block IF')
elif number == 4:
    print('Hello')
    print('Block ELIF')
    #блок выполнения условия не может быть пустым. можно указывать pass если ничего не нужно
else:
    print('Block ELSE')

print(number)

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')



#CYCLES

l = []
i = 2
while i <= 1024:
    l = l + [i]
    i = i * 2
print(l)



seq = [1,2,3,4,5,6]
for l in seq:
    print(l)

mydict = {"kostya": 1, "anna": 2, "alex": 3}
for key in mydict:
    print(key)
    print(mydict[key])

pairs = [(1,2),(3,4),(5,6)]
for item in pairs:
    print(item)


for (t1, t2) in pairs:
    print('T1: ',t1)
    print('T2: ',t2)

print('\n')
print('\n')

x = [1,2,3,4]
out = [(num ** 2 for num in x)]
print(out)

for i in 'Helo world!':
    if i == 'o':
        continue
    print (i * 2, end='')
print(i)


for i in 'Helo world!':
    if i == 'o':
        break
    print (i * 2, end='')
print(i)

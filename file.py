#FILES

# sys.stdin
# sys.stdout
# sys.stderr

f = open('data.txt', 'w')
f.write('#Name Email Phone\n')
f.write('Kostya kostya@mail.ru 111-1111\n')
f.write('Admin admin@iir.ua 124-15151\n')
f.write('Supp support@mail.ru 1451-5115\n')
f.close()

#тоже самое
f = open('data.txt', 'w')
try:
    f.write('#Name Email Phone\n')
    f.write('Kostya kostya@mail.ru 111-1111\n')
    f.write('Admin admin@iir.ua 124-15151\n')
    f.write('Supp support@mail.ru 1451-5115\n')
finally:
    f.close()

#тоже самое
with open('data.txt', 'w') as f:
    f.write('#Name Email Phone\n')
    f.write('Kostya kostya@mail.ru 111-1111\n')
    f.write('Admin admin@iir.ua 124-15151\n')
    f.write('Supp support@mail.ru 1451-5115\n')

f1 = open('data1.txt', 'w')
f1.writelines(['11111\n', '222222\n'])
f1.close()

f2 = open('data.txt')
print(f2.read())

f2 = open('data.txt')
print(f2.read(1))

f2 = open('data.txt')
print(f2.readline())

f2 = open('data.txt')
print(f2.readlines())

f2 = open('data.txt') #считывать файл с 8й позиции
f2.seek(8)
print(f2.read())


f2 = open('data.txt')
for line in f2:
    print(line)

f2 = open('data.txt')
for line in f2:
    print(line, end='')
#то же самое
for line in open('data.txt'):
    print(line, end='')

print('\n')
print('\n')
print('\n')


fin = open('data.txt', 'r')
buf = fin.readlines()
fin.close()
buf.sort()
fout = open ('data2.txt', 'w')
for line in buf:
    fout.write(line)
    print(line, end='')
fout.close()



print('\n')
print('\n')
print('\n')




f = open('data.txt')
content = f.read()
f.close()
words = content.split()
print(words, end='\n')
print('There are {0} words in the file'.format(len(words)))

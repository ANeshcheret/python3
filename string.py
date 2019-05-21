python = 'Python\'3.7.1\''
django = "Django \"1.11\""
print (python)
print ("Hello\nDjango")


print(str)

s1 = "Python12345"
s2 = 'python3.7.1'

print (s1 + s2)
print (s1 * 2)
print(s1[0])
print (s1[2] + s1[5])
print (s1[-2])
# string[start:stop]
print(s1[1:4])
print(s1[3:])
print(s1[:3])
print(s1[::-1])
# string[start:stop:stride]
print(s1[1:10:2])
print('\n', len(s1), '\n')
print(s1.upper())
print(s1.lower())
print(s2.capitalize())

s3 = "Hello Pythons"

print(s3.split())

print(s3.split('o'))

s4 = "Hello, {} and {}".format("Kostya", "Anna")
print(s4)

s5 = "Hello, {a} and {k}".format(k = "Kostya", a = "Anna")
print(s5)

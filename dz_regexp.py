##LAST WORD
import re
pattern =r'\w+$'
text = 'Subscribe to pythons insider via RSS'
result = re.findall(pattern, text)
print(result)

##два последовательных символа
pattern = r'\b\w.'
text = 'Subscribe to pythons insider via RSS'
result = re.findall(pattern, text)
print(result)

#список доменов из списка адресов электронной почты
pattern = r'@\w+.\w+'
text = 'my.test@mail.com, ee.fg@i.ua, tgw4q@ukr.net'
result = re.findall(pattern, text)
print(result)


pattern = r'@\w+.(\w+)'
text = 'my.test@mail.com, ee.fg@i.ua, tgw4q@ukr.net'
result = re.findall(pattern, text)
print(result)

# 1. Извлечь дату из строки.
# 2. Извлечь только год из строки.
pattern = r'\d{2}-\d{2}-(\d{4})'
text = 'Amit 35-3557 25-04-2017, XYZ 56-4633 23-01-2014, ABC 68-8046 28-02-2016'
result = re.findall(pattern, text)
print(result)



# Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9):
# Подсказка: используйте for-in, re.match() и len()
# Результат - no, yes, no

pattern = r''
text = ['8123456-123', '8123456789', '912345x1234']

for value in text:
    if re.match(r'[8-9]{1}[0-9]{9}', value) and len(value) == 10:
        print('yes')
    else:
        print('no')

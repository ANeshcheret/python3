import re
# pattern = r'[0-9]+'
# text = '123423tttt23 trgf13 1234 f13 fasdfg 1151'
# number_re = re.compile(pattern)
# print(number_re.findall(text))


# import re
# pattern = r'[0-9]+'
# text = '123423tttt23 trgf13 1234 f13 fasdfg 1151'
# print(re.findall(pattern, text))


# pattern = '@'
# email = 'test@mail.ru'
# print(re.split(pattern, email))


# pattern = ['Python', 'Django']
# text = 'A string for test. Im searching for Python 3.7.1'
# for p in pattern:
#     print("I'm searching for: " + p)
#     if re.search(p, text):
#         print('Match')
#     else:
#         print('Not match')


# text = 'A string for test. Im searching for Python 3.7.1'
# match = re.search('Python', text)
# print(match.start()) #находит Python на 36й позиции текста


def print_findall(pattern, text):
    for p in pattern:
        print('Seaching for pattern {}'.format(p))
        print(re.findall(p, text))
        print('\n')


# test_pattern = ['[a[ab]+]']
# test_text = 'ababbdf....bfsb...aaaabbbb...ewrfasaaadva...abababab'
# print_findall(test_pattern, test_text)

# test_pattern = ['[^!.?]+']
# test_text = 'This is a string! But is has punctuation. How can we remove it?'
# print_findall(test_pattern, test_text)

# test_pattern = ['[A-Z]+']
# test_text = 'This is a string! But is has punctuation. How can we remove it?'
# print_findall(test_pattern, test_text)


test_pattern = ['\\W+'] #[r'\d+']
test_text = 'This is a string with a numbers 2142342312351 with a symbol #Python'
print_findall(test_pattern, test_text)

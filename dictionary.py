mydict = {}
mydict = {'key1':'value1', 'key2':'value2'}
print(mydict['key1'])
mydict['key2'] = 123
print(mydict['key2'])
print(mydict)
mydict['key3'] = 'value3'
print(mydict)



d2 = {'key1': 123, 'key2': 'value4', 'key3': {'123': [1,2,'find me']}}
print(d2['key3']['123'][2]) # find find me
print(d2['key3']['123'][2].upper()) # UP register

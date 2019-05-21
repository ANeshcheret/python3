#Seryyzatsia desirilizatsya

import pickle

obj = {'one': 123, 'two':[1,2,3]}
output = pickle.dumps(obj, 3)
print(output)

obj1 = pickle.loads(output)
print(obj1)

data = {'a': [1,2.0,4+6j], 'b': ('character', 'string', 'test'), 'c': {None, True, False}}

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    data_new = pickle.load(f)
print(data_new)

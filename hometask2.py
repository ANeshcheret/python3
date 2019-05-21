####1
# a = input('Enter some nubers:')
# b = list(map(int, a))
# print(b)
# for i in range(len(b) - 1):
#     print(i)
# for i in range(len(b) - 1):
#     if b[i]==1 and b[i+1]==2 and b[i+2]==3:
#         print(b[i], '\n')
#         print(b[i+1], '\n')
#         print(b[i+2], '\n')
#         break
#     else:
#         print(False)


def listCheck(nums):
    for i in range(len(nums) - 1):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
            continue
        return False
print(listCheck([1,2,3,1,5,6]))
print(listCheck([1,1,3,1,5,6]))

print('\n')
########
######2
def stringBits(mystring):
    result = ''

    for a in range(len(mystring)):
        if a % 2 == 0:
            result = result + mystring[a]
    return result
print(stringBits('Heeololeo'))

def stringBits(mystring):
    result = ''

    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i]
    return result

print(stringBits('Heeololeo'))

print('\n')
####3
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-len(a):]

print(end_other('abc', 'abXacvabc'))

print('\n')
#####4
def doubleChar (mystring):
    result = ''
    for i in mystring:
        result = result + i * 2
    return result

print(doubleChar('fksf gw argo '))

print('\n')

###5
def count_events(nums):
    a = 0
    for i in nums:
        if i % 2 == 0:
            a += 1
    return a

print(count_events([2,2,4,6,1,3]))

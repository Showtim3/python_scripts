print('Hi bro')

x = False

if x:
    print('True is run')
else:
    print('Hey bro')

numberList = [1, 20, 4, 5, 9, 19]

for number in numberList:
    print(number)

nameString = 'This stuff looks easy'

for char in nameString:
    print(char)

tupleList = [(1, 2), (3, 4), (10, 11)]

for tup in tupleList:
    print tup

for a, b in tupleList:
    print b

print(len(tupleList))

dict = {'k1': 1, 'k2': 11, 'k3': 211}

for item in dict:
    print(item)

for item in dict.items():
    print(item)

for key, value in dict.items():
    print value
# this is a comment

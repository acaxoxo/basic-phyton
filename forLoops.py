# Introduction to For Loops

list1 = ['apples', 'bananas', 'cherries']
tup1 = (2, 6, 10)

for item in list1:
    print(item)

for item in tup1:
    print(item)

###

for i in range(0, 10):
    print(i)

###

for i in range(1, 11):
    print(i)

###

for i in range(0, 11, 2):
    print(i)

###

for i in range(5, 51, 5):
    print(i)

###

for i in range(0, 5):
    print(i)

###
print()
print()

for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)
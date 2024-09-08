# Welcome to Dictionaries!

students = ['bob', 12, 'rachel', 13, 'emily', 15]
print(students)

###

students = {'bob': 12, 'rachel': 13, 'emily': 15}
print(students)
print(students['rachel'])
print(students['bob'])

###

students['rachel'] = 14
print(students)

### 

del students['emily']
print(students)

###

print(len(students))

###

students = {'bob': 12, 'bob': 13, 'bob': 15}
print(students) 
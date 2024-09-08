# Conditional Statements

if 5 > 3:
  print("hello")
  
###

if 3 < 2:
  print("hello")
else:
  print("condition was not true")

# relation operators
# > < >= <= == !=

# Uncomment the below to see the error
# if 5 = 3:
#   print('hello')

###

if 5 == 3:
  print('hello')
  
###

age = 16
if age <= 15:
  print("You are younger than 16")
elif age == 16:
  print("You are 16")
elif age == 17:
  print("You are 17")
else:
  print("You are older than 16")
  
###

age = 16
if age < 13:
  print("You are a child")
elif age >= 13 and age < 18:
  print("You are a teenager")
else:
  print("You are an adult")

###

if 5 > 3 or 2 < 1:
  print("hi")
# Welcome to Functions!

def hello_world():
  print("Hello World")
  
hello_world()

###

def greeting(name):
  print("Hi " + name + "!")

greeting("Avi")

###

def add(num1, num2):
  print(num1 + num2)

add(10, 15)

###

def add(num1, num2):
  return num1 + num2

num_sum = add(12, 34)
print(num_sum)

def mul(num1, num2):
  return num1 * num2
  print("hello") # would not be run

print(mul(add(1, 2), add(3, 4)))
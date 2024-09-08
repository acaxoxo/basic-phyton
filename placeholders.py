# Placeholders in Strings

name = "jake"
print(name + " is 15 years old")

###

name = "jake"
sentence = "%s is 15 years old"
print(sentence % name)

###

sentence = "%s %s was the president of the United States"
print(sentence % ("Barack", "Obama"))

###

sentence = "%s is %d years old"
print(sentence & ("avi", 23))

###

name = "avi"
print(f"Hello, {name}")

###

x = 10
y = 20
print(f"The sum of x and y is {x + y}")
# Introduction to Lists

item1 = 'apples'
item2 = 'oranges'
item3 = 'bananas'
item4 = 'cheese'

###

shopping_list = ['apples', 'oranges', 'bananas', 'cheese']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[2])
print(shopping_list[0:2])
print(shopping_list[0:3])

###

shopping_list.append('blueberries') # add items
print(shopping_list)

###

shopping_list[0] = 'cherries' # update items
print(shopping_list)

###

del shopping_list[1] # delete items
print(shopping_list)

###

print(len(shopping_list)) # length of list

###

shopping_list2 = ['bread', 'jam', 'pb']
print(shopping_list + shopping_list2)
print(shopping_list * 2)

###

list_num = [1,4,7,23,6]
print(max(list_num))
print(min(list_num))
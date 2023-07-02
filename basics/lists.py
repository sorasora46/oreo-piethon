food = ["noodles", "spaghetti", "fried rice"]

print(food[0])
print(food[len(food) - 1])

for i in range(len(food)):
    print(food[i], "", end="")
print()

# or
for i in food:
  print(i)

# append (insert at the end)
food.append('ice cream')

# remove
food.remove('noodles')

# pop remove last element
food.pop()

# insert at specific location
food.insert(0, 'cake')

# sort the list
food.sort()

# clear a list
food.clear()

# 2D lists
list_a = [5, 13, 34]
list_b = ['hi', 'hello']
lists_of_lists = [list_a, list_b]
print(lists_of_lists)

for list in lists_of_lists:
   for item in list:
    print('item in the list is', item)
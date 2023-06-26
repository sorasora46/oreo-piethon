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
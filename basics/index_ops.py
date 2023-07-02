# index operator [] = gives access to a sequence's element (string, list, tuples)

# [inclusive:exclusive]

name = 'sorrawit kwnaja'

first_name = name[:(name.find(' '))].upper()
# same with name[0:3]
last_name = name[(name.find(' ') + 1):].upper()

# or just use split
first_and_last = name.split(' ')

print(first_name)
print(last_name)

print(first_and_last[0].upper())
print(first_and_last[1].upper())
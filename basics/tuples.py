# tuple = collection which is ordered and unchangeable, used to group together related data

user = ('Sorrawit Kwanja', 20, 'Student')
print(user)

print(user.count('Student'))
print(user.index('Student'))

# for loop in tuple
for data in user:
  print(data)

# check if the item exist in tuple
if 'Student' in user:
  print('This user is a student.')
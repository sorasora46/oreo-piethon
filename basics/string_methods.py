str_data = 'lorem lorem lorem'

# length
print(len(str_data))

# find
print(str_data.find('l'))

# capitalize first char
print(str_data.capitalize())

# upper
print(str_data.upper())

# lower
print(str_data.lower())

# check if string is number
print(str_data.isdigit())

# check if string contains only letters
print(str_data.isalpha())

# count the letters in the string
print(str_data.count('l'))

# replace letters (replace all)
print(str_data.replace('l', 'x'))

# slicing string

name = 'aaaaa bbbbb ee qqqq'

# access char within string just like c
char1 = name[0] # <- char1 = a

# slice by indexing[] [start:stop:step]
# first index is inclusive
# last index is exclusive
section1 = name[0:4]
section2 = name[:4] # work the same for above and the other way around
section3 = name[0:8:2] # step means every that step in string
print(section1)

# reverse a string
reverse = name[::-1]
print(reverse)

# slice()
url = 'https://www.youtube.com'

slice1 = slice(12, -4, 1)
print(url[slice1])
data = 5

# all data types:
# int
# float
# str

# use type(data) to check the type
print('type():' , type(data))

print(type(int(data)))
print(type(float(data)))
print(type(str(data)))

# cannot perform math ops on str (be careful!)
print("3"*3)
print(int("3") * 3)
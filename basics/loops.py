import time
# while loop
# execute as long as condition is true

n = int(input('Enter number: '))

i = 1
# count number to n
while i <= n:
  print('index:', i)
  i += 1

str = input('Enter string less than 5 characters: ')
if len(str) < 5:
  l = 0
  while l < len(str):
    print(str[l])
    l += 1

name = '' 
while len(name) == 0:
  name = input('Enter your name: ')
print(name)
# or u can do this
# name = None
# while not name:

# for loop
# execute with defined condition (already know how many time to iterate)
for index in range(10):
  print(index)

for index in range(10, 50): # range(inclusive, exclusive)
  print(index)

for index in range(10, 50, 2): # count up by 2
  print(index)

for index in range(10, 50, -2): # count down by 2
  print(index)

for index in 'Hi, My name is Boss.':
  print(index)

for second in range(10, 0, -1):
  print(second)
  time.sleep(1) # in second

for m in range(10):
  for n in range(10):
    print('#', end='')
  print(end='\n')


# loop control statements
# break, continue, pass (pass does nothing)

# break
for n in range(10):
  if n == 5:
    print('Hi!')
    break
  print(n)
  n += 1

# continue
for n in range(10):
  if n == 5:
    print('Hi!')
    continue
  print(n)
  n += 1
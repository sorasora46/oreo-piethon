# use input() for prompting user for input
name = input('what is your name?: ')
print('hello,', name)

# input() always return string!
number = input('get number: ')
print(type(number))
print(type(int(number)))

# string concatenation only work with string
# if number is numeric data then it's error
print('the number is ', number, '!!!')

# use this when taking input
# int(input())
# float(input())
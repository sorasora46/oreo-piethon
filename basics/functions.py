def foo():
    print('foo')

foo()

for i in range(10):
  foo()

def greeting(name):
  print('Hello, ' + name + '!')

greeting('Boss')

def fib(number):
  if number <= 2:
     return 1
  return fib(number - 1) + fib(number - 2)

print(fib(10))

# keyword argument (label the argument when passing to the function)
def prism(width, height, length):
  return 2 * ((width * height) + (height * length) + (height * width))
print(prism(height=5, width=20, length=12))

# variable-length arguments
# *args = parameter that will pack all arguments into a 'tuple'
# useful so that a function can accept a varying amount of arguments
# make sure to have asterisk (*)

def add(*numbers):
  sum = 0
  num_list = list(numbers) # should be cast to a list because tuple does not allow item assigment
  for i in num_list:
    sum += i
  return sum

print(add(5,12,34))

# keyword arguments
# **kwargs = packed all argument into map like taking all argument into json
# need to have 2 asterisks (**)

def func1(**kwargs):
  x = kwargs.get('x')
  y = kwargs.get('y')
  z = kwargs.get('z')
  print(kwargs.keys())
  print('value of x y z', x, y, z)

func1(x = 5, y = 10, z = 20)
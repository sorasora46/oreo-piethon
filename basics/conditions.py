age = int(input('What is your age?: '))

# and + elif + else
if age >= 18:
    print('Legal')
elif age >= 16 and age < 18:
    print('Maybe Legal')
else:
    print('Illegal')

# or
num = int(input('Enter number: '))

if num == 20 or num % 2 == 0:
    print('Cool')

# not
if not(num % 2 == 0):
    print('Can\'t devided by 2')
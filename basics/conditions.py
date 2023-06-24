age = int(input('What is your age?: '))

if age >= 18:
    print('Legal')
elif age >= 16 and age < 18:
    print('Maybe Legal')
else:
    print('Illegal')
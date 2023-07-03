
name = 'Boss'
job = 'Student'
age = 18

print('My name is {}. I am a {} and I am {} years old.'.format(name, job, age))
print('My name is {1}. I am a {2} and I am {0} years old.'.format(name, job, age)) # with positional argument
print('argument 1 {arg1}. argument 2 {arg2}'.format(arg1 = 'HI', arg2 = 'HELLO'))

# add padding to the string
print('sdljaslkdgjasdklg {} sljgdskdg'.format('Boss Sorrawit Kwanja'))
print('sdljaslkdgjasdklg {:10} sljgdskdg'.format('Boss Sorrawit Kwanja'))
print('sdljaslkdgjasdklg {:<10} sljgdskdg'.format('Boss Sorrawit Kwanja')) # align left
print('sdljaslkdgjasdklg {:>10} sljgdskdg'.format('Boss Sorrawit Kwanja')) # align right
print('sdljaslkdgjasdklg {:^10} sljgdskdg'.format('Boss Sorrawit Kwanja')) # center text

# formatting number
pie = 3.14159
money = 100000
print('pie is {:.2f}'.format(pie))
print('money = {:,}'.format(money))
print('binary = {:b}'.format(256)) # binary
print('octal = {:o}'.format(256)) # octal
print('hex = {:X}'.format(256)) # or :x for hex with lowercase
print('scientific notation = {:E}'.format(129000000000000000)) # or :e for lowercase

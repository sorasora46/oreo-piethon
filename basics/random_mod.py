import random # pseudo random number

for i in range(10):
  x = random.randint(1, 6) # random integer from 1 - 6
  print(x)

print(random.random())

# generate random choice from list
list = ['rock', 'scissors', 'paper']

for i in range(5):
  print(random.choice(list))

# shuffle the list
cards = []
for i in range(52):
  cards.append(i + 1)

print(cards)
random.shuffle(cards)
print(cards)
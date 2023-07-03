
try:
  numerator = int(input('Enter numerator: '))
  denominator = int(input('Enter denominator: '))
  result = numerator / denominator
except ZeroDivisionError as e:
  print('Divided by 0')
  print(e)
except ValueError as e:
  print('Wrong input type')
  print(e)
except Exception as e:
  print('Something went wrong :(')
  print(e)
else: # if no error
  print(result)
finally: # execute whether or not error occur always execute
  print('Executed')
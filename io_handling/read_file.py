import os

path = 'C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example.txt'

if os.path.exists(path):
  with open(path) as file:
    print(file.read())
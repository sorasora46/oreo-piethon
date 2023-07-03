import os

# if backslash (\) in file, add one more
path = 'C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example.txt'
path2 = 'C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example'

if os.path.exists(path):
    print('path exist')
    if os.path.isfile(path):
      print('it is a file')
    if os.path.isfile(path2):
      print('it is a file')
    else:
      print('it is not a file')
    if os.path.isdir(path2):
       print('it is a directory')
else:
    print('file not found')
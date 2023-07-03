try:
    # write to file
    with open('C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example.txt', 'w') as file:
      text = 'Hi! \nMy name is Boss.'
      file.write(text)
    # append to file
    with open('C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example.txt', 'a') as file:
      text = '\nThis message should append at the end of the file'
      file.write(text)
except FileNotFoundError as e:
   print(e)
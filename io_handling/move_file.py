import os

source = '/home/sora/Projects/learn-python/io_handling/need_move_file.txt'
dest = '/home/sora/Projects/learn-python/io_handling/moved_folder/need_move_file.txt'

try:
    if os.path.exists(dest):
        print('File already exist')
    else:
        os.replace(source, dest)
        print('File was moved')
except FileNotFoundError as e:
    print(e)


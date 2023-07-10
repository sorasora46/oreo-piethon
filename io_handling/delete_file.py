import os
import shutil

path = '/home/sora/Projects/learn-python/io_handling/delete_me.txt'
path2 = '/home/sora/Projects/learn-python/io_handling/delete_me'
path3 = '/home/sora/Projects/learn-python/io_handling/delete_me2'

try:
    if os.path.exists(path):
        os.remove(path)
    os.rmdir(path2) # for deleting empty folder
    shutil.rmtree(path3) # same for rm -rf
except FileNotFoundError as e:
    print(e)
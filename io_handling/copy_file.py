# copyfile() copies content of a file
# copy() copyfile() + permission mode + destination
# copy2() copy() + copies metadata

import shutil

filepath = 'C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\example.txt'
copied_name = 'example2_with_copyfile.txt'
dest = 'C:\\Users\\sorra\\codes\\oreo-piethon\\io_handling\\' + copied_name

shutil.copyfile(filepath, dest)
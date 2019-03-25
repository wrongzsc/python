#
# @encoding: utf-8
# @Author: wrong.zsc 
# @Date: 2018-04-08 00:11:01 
#

import os
import time

# 1.the files and dictionaries to be backed up are specified in a list
source = [
    '"C:\\Users\\zheng\\OneDrive\\Python"',
    #   'C:\\Users\\zheng\\OneDrive\\Python\\book'
]
# notice we had to use double quotes inside the string for names with it
#   spaces in it.

# 2.the backup must be stored in a main backup directory
target_dir = 'C:\\backup'  # remember to change this to what you will be
#   using

# 3.the files are backed up into a zip file.
# 4.the name of the zip is the current date and time

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5.we use the zip cpmmand to put the files in a zip archive

zip_command = "Bandizip -qr {0}{1}".format(
    target, ''.join(source))  
#   未安装zip bandizip无法使用命令？

# run the backup
print(zip_command)
if os.system(zip_command) == 0:
    print('successfully back up to', target)
else:
    print('backup failed')

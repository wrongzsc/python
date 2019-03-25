import sys
import os

print(os.getcwd())

print('the command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\n the path is ', sys.path, '\n')

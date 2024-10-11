# Extracted from https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments
#!/usr/bin/python

import sys

print 'Number of arguments entered :' len(sys.argv)

print 'Your argument list :' str(sys.argv)

python arguments_List.py chocolate milk hot_Chocolate

Number of arguments entered : 4
Your argument list : ['arguments_List.py', 'chocolate', 'milk', 'hot_Chocolate']


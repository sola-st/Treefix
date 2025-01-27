# Extracted from https://stackoverflow.com/questions/493386/how-to-print-without-a-newline-or-space
def Print(s):
    return sys.stdout.write(str(s))

for i in range(10): # Or `xrange` for the Python 2 version
    Print(i)

0123456789


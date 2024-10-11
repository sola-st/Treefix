# Extracted from https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
def myfunc(**kwargs):
for k,v in kwargs.items():
   print("%s = %s" % (k, v))

myfunc(abc=123, efh=456)
# abc = 123
# efh = 456

def myfunc2(*args, **kwargs):
   for a in args:
       print(a)
   for k,v in kwargs.items():
       print("%s = %s" % (k, v))

myfunc2(1, 2, 3, banan=123)
# 1
# 2
# 3
# banan = 123


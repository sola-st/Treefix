# Extracted from https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print
class Test(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        return "An instance of class Test with state: a=%s b=%s" % (self._a, self._b)

    def __repr__(self):
        return 'Test("%s","%s")' % (self._a, self._b)

x = Test('hello', 'world')
print 'Human readable: ', str(x)
print 'Object representation: ', repr(x)
print

y = eval(repr(x))
print 'Human readable: ', str(y)
print 'Object representation: ', repr(y)
print

Human readable:  An instance of class Test with state: a=hello b=world
Object representation:  Test("hello","world")

Human readable:  An instance of class Test with state: a=hello b=world
Object representation:  Test("hello","world")


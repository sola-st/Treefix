# Extracted from https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
class Test(object):
    def __init__(self):
        self.__a = 'a'
        self._b = 'b'

t = Test()
t._b
'b'

t.__a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test' object has no attribute '__a'

t._Test__a
'a'


# Extracted from https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
class A(object):
a = A()
print a.__str__()
('a', 'b')
print str(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __str__ returned non-string (type tuple)


# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
class Person(_n_(821919, "object", lambda: object)):
   def __init__(self, name, age):
       _n_(821920, "self", lambda: self).name = _n_(821921, "name", lambda: name)
       _n_(821922, "self", lambda: self).age = _n_(821923, "age", lambda: age)

   def __eq__(self, other):
       return _a_(821925, _n_(821924, "self", lambda: self), "name") == _a_(821927, _n_(821926, "other", lambda: other), "name") and _a_(821929, _n_(821928, "self", lambda: self), "age") == _a_(821931, _n_(821930, "other", lambda: other), "age")

jack1 = _c_(821933, _n_(821932, "Person", lambda: Person), 'Jack', 23)
jack2 = _c_(821935, _n_(821934, "Person", lambda: Person), 'Jack', 23)

_n_(821936, "jack1", lambda: jack1) == _n_(821937, "jack2", lambda: jack2) # True
_n_(821938, "jack1", lambda: jack1) is _n_(821939, "jack2", lambda: jack2) # False


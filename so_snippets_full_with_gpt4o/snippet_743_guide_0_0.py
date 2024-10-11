class Bar: # pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python
from l3.Runtime import _l_
print(foo = 1+3)
_l_(13855)

class Foo(Bar):
    _l_(13856)

pass

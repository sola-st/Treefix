from typing import Any # pragma: no cover
class Bar: pass # pragma: no cover

foo = 1 + 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python
from l3.Runtime import _l_
print(foo = 1+3)
_l_(2322)

class Foo(Bar):
    _l_(2323)

pass

class MockObject:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
self = MockObject() # pragma: no cover
name = 'example_attribute' # pragma: no cover
value = 42 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.__dict__[name] = value
_l_(22877)

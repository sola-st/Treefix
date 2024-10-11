# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
from l3.Runtime import _l_
class A:
    _l_(2333)

    instance = None
    _l_(2332)
A.instance = A()
_l_(2334)


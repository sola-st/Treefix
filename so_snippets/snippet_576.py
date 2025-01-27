# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3278077/difference-between-getattr-and-getattribute
from l3.Runtime import _l_
class SomeObject(object):
    _l_(2496)

    pass
    _l_(2495)

class SubObject(SomeObject):
    _l_(2498)

    pass
    _l_(2497)

class SomeObject:
    _l_(2500)

    pass
    _l_(2499)


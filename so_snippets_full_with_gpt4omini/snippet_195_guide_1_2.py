class C: pass # pragma: no cover
class C1(C): pass # pragma: no cover
class C2(C): # pragma: no cover
    i = 2 # pragma: no cover
class C12(C1, C2): pass # pragma: no cover
class C21(C2, C1): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
from l3.Runtime import _l_
class C:
    _l_(2997)

i = 0class C1(C):
    _l_(2998)

passclass C2(C):
    _l_(2999)

i = 2class C12(C1, C2):
    _l_(3000)

passclass C21(C2, C1):
    _l_(3001)

pass
assert C12().i == 0
_l_(3002)
assert C21().i == 2
_l_(3003)

try:
    _l_(3008)

    C12.__mro__
    _l_(3004)
except AttributeError:
    _l_(3006)

    pass
    _l_(3005)
else:
    assert False
    _l_(3007)

class C(object):
    _l_(3009)

i = 0class C1(C):
    _l_(3010)

passclass C2(C):
    _l_(3011)

i = 2class C12(C1, C2):
    _l_(3012)

passclass C21(C2, C1):
    _l_(3013)

pass
assert C12().i == 2
_l_(3014)
assert C21().i == 2
_l_(3015)

assert C12.__mro__ == (C12, C1, C2, C, object)
_l_(3016)
assert C21.__mro__ == (C21, C2, C1, C, object)
_l_(3017)

# OK, old:
class Old:
    _l_(3018)

passtry:
    _l_(3023)

    raise Old()
    _l_(3019)
except Old:
    _l_(3021)

    pass
    _l_(3020)
else:
    assert False
    _l_(3022)

# TypeError, new not derived from `Exception`.
class New(object):
    _l_(3024)

passtry:
    _l_(3029)

    raise New()
    _l_(3025)
except TypeError:
    _l_(3027)

    pass
    _l_(3026)
else:
    assert False
    _l_(3028)

# OK, derived from `Exception`.
class New(Exception):
    _l_(3030)

passtry:
    _l_(3035)

    raise New()
    _l_(3031)
except New:
    _l_(3033)

    pass
    _l_(3032)
else:
    assert False
    _l_(3034)

# `'str'` is a new style object, so you can't raise it:
try:
    _l_(3040)

    raise 'str'
    _l_(3036)
except TypeError:
    _l_(3038)

    pass
    _l_(3037)
else:
    assert False
    _l_(3039)


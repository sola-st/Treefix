# Corrected indentation and formatting for the provided code snippet # pragma: no cover
class C:# pragma: no cover
    i = 0 # pragma: no cover
class C1(C):# pragma: no cover
    pass # pragma: no cover
class C2(C):# pragma: no cover
    i = 2 # pragma: no cover
class C12(C1, C2):# pragma: no cover
    pass # pragma: no cover
class C21(C2, C1):# pragma: no cover
    pass # pragma: no cover
class C(object):# pragma: no cover
    i = 0 # pragma: no cover
class C1(C):# pragma: no cover
    pass # pragma: no cover
class C2(C):# pragma: no cover
    i = 2 # pragma: no cover
class C12(C1, C2):# pragma: no cover
    pass # pragma: no cover
class C21(C2, C1):# pragma: no cover
    pass # pragma: no cover
class Old:# pragma: no cover
    pass # pragma: no cover
class New(object):# pragma: no cover
    pass # pragma: no cover
class New(Exception):# pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
from l3.Runtime import _l_
class C:
    _l_(14718)

i = 0class C1(C):
    _l_(14719)

passclass C2(C):
    _l_(14720)

i = 2class C12(C1, C2):
    _l_(14721)

passclass C21(C2, C1):
    _l_(14722)

pass
assert C12().i == 0
_l_(14723)
assert C21().i == 2
_l_(14724)

try:
    _l_(14729)

    C12.__mro__
    _l_(14725)
except AttributeError:
    _l_(14727)

    pass
    _l_(14726)
else:
    assert False
    _l_(14728)

class C(object):
    _l_(14730)

i = 0class C1(C):
    _l_(14731)

passclass C2(C):
    _l_(14732)

i = 2class C12(C1, C2):
    _l_(14733)

passclass C21(C2, C1):
    _l_(14734)

pass
assert C12().i == 2
_l_(14735)
assert C21().i == 2
_l_(14736)

assert C12.__mro__ == (C12, C1, C2, C, object)
_l_(14737)
assert C21.__mro__ == (C21, C2, C1, C, object)
_l_(14738)

# OK, old:
class Old:
    _l_(14739)

passtry:
    _l_(14744)

    raise Old()
    _l_(14740)
except Old:
    _l_(14742)

    pass
    _l_(14741)
else:
    assert False
    _l_(14743)

# TypeError, new not derived from `Exception`.
class New(object):
    _l_(14745)

passtry:
    _l_(14750)

    raise New()
    _l_(14746)
except TypeError:
    _l_(14748)

    pass
    _l_(14747)
else:
    assert False
    _l_(14749)

# OK, derived from `Exception`.
class New(Exception):
    _l_(14751)

passtry:
    _l_(14756)

    raise New()
    _l_(14752)
except New:
    _l_(14754)

    pass
    _l_(14753)
else:
    assert False
    _l_(14755)

# `'str'` is a new style object, so you can't raise it:
try:
    _l_(14761)

    raise 'str'
    _l_(14757)
except TypeError:
    _l_(14759)

    pass
    _l_(14758)
else:
    assert False
    _l_(14760)


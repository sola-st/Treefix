import sys # pragma: no cover
from types import ModuleType # pragma: no cover

sys.modules['test'] = ModuleType('test') # pragma: no cover
sys.modules['test.a'] = ModuleType('test.a') # pragma: no cover
sys.modules['test.b'] = ModuleType('test.b') # pragma: no cover
def mocked_b2(): print('mocked b2') # pragma: no cover
sys.modules['test.b'].b2 = mocked_b2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9252543/what-can-i-do-about-importerror-cannot-import-name-x-or-attributeerror
from l3.Runtime import _l_
try:
    from test.b import b2
    _l_(12263)

except ImportError:
    pass

def a1():
    _l_(12266)

    print('a1')
    _l_(12264)
    b2()
    _l_(12265)
try:
    from test.a import a1
    _l_(12268)

except ImportError:
    pass

def b1():
    _l_(12271)

    print('b1')
    _l_(12269)
    a1()
    _l_(12270)

def b2():
    _l_(12273)

    print('b2')
    _l_(12272)

if __name__ == '__main__':
    _l_(12275)

    b1()
    _l_(12274)

def a1():
    _l_(12278)

    print('a1')
    _l_(12276)
    b2()
    _l_(12277)
try:
    from test.b import b2
    _l_(12280)

except ImportError:
    pass

b1
_l_(12281)
a1
_l_(12282)
b2
_l_(12283)


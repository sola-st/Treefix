def a1(): print('a1'); b2() # pragma: no cover
def b1(): print('b1'); a1() # pragma: no cover
def b2(): print('b2') # pragma: no cover
b1() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9252543/what-can-i-do-about-importerror-cannot-import-name-x-or-attributeerror
from l3.Runtime import _l_
try:
    from test.b import b2
    _l_(297)

except ImportError:
    pass

def a1():
    _l_(300)

    print('a1')
    _l_(298)
    b2()
    _l_(299)
try:
    from test.a import a1
    _l_(302)

except ImportError:
    pass

def b1():
    _l_(305)

    print('b1')
    _l_(303)
    a1()
    _l_(304)

def b2():
    _l_(307)

    print('b2')
    _l_(306)

if __name__ == '__main__':
    _l_(309)

    b1()
    _l_(308)

def a1():
    _l_(312)

    print('a1')
    _l_(310)
    b2()
    _l_(311)
try:
    from test.b import b2
    _l_(314)

except ImportError:
    pass

b1
_l_(315)
a1
_l_(316)
b2
_l_(317)


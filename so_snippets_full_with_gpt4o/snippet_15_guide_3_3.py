import sys # pragma: no cover
import types # pragma: no cover

helper = None # pragma: no cover
TestPy = types.ModuleType('TestPy') # pragma: no cover
sys.modules['TestPy'] = TestPy # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
from l3.Runtime import _l_
def five(enterAnumber,sumation):
    _l_(11882)

    global helper
    _l_(11880)
    helper  = enterAnumber + sumation
    _l_(11881)

def isTheNumber():
    _l_(11884)

    aux = helper
    _l_(11883)
    return aux
try:
    import TestPy
    _l_(11886)

except ImportError:
    pass

def main():
    _l_(11890)

    atest  = TestPy
    _l_(11887)
    atest.five(5,8)
    _l_(11888)
    print(atest.isTheNumber())
    _l_(11889)

if __name__ == '__main__':
    _l_(11892)

    main()
    _l_(11891)


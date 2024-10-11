helper = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
from l3.Runtime import _l_
def five(enterAnumber,sumation):
    _l_(50)

    global helper
    _l_(48)
    helper  = enterAnumber + sumation
    _l_(49)

def isTheNumber():
    _l_(52)

    aux = helper
    _l_(51)
    return aux
try:
    import TestPy
    _l_(54)

except ImportError:
    pass

def main():
    _l_(58)

    atest  = TestPy
    _l_(55)
    atest.five(5,8)
    _l_(56)
    print(atest.isTheNumber())
    _l_(57)

if __name__ == '__main__':
    _l_(60)

    main()
    _l_(59)


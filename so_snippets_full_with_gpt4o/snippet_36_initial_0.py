class ChildB:# pragma: no cover
    def __call__(self):# pragma: no cover
        print('ChildB instance called') # pragma: no cover
class ChildA:# pragma: no cover
    def __call__(self):# pragma: no cover
        print('ChildA instance called') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
from l3.Runtime import _l_
Base = ChildB
_l_(13351)

Base()
_l_(13352)

Base = ChildA
_l_(13353)

Base()
_l_(13354)


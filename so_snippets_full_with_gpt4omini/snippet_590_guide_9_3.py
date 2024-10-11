# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
from l3.Runtime import _l_
class Foo:
    _l_(2293)

    def __eq__(self, other):
        _l_(2292)

        if isinstance(other, self.__class__):
            _l_(2291)

            aux = self.__dict__ == other.__dict__
            _l_(2289)
            return aux
        else:
            aux = False
            _l_(2290)
            return aux

class Bar(Foo):
    _l_(2294)

pass
b = Bar()
_l_(2295)
f = Foo()
_l_(2296)
f == b
_l_(2297)
True
_l_(2298)
b == f
_l_(2299)
False
_l_(2300)

def __eq__(self, other):
    _l_(2304)

    if type(other) is type(self):
        _l_(2302)

        aux = self.__dict__ == other.__dict__
        _l_(2301)
        return aux
    aux = False
    _l_(2303)
    return aux


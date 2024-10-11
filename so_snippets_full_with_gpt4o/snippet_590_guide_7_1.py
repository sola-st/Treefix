# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
from l3.Runtime import _l_
class Foo:
    _l_(13760)

    def __eq__(self, other):
        _l_(13759)

        if isinstance(other, self.__class__):
            _l_(13758)

            aux = self.__dict__ == other.__dict__
            _l_(13756)
            return aux
        else:
            aux = False
            _l_(13757)
            return aux

class Bar(Foo):
    _l_(13761)

pass
b = Bar()
_l_(13762)
f = Foo()
_l_(13763)
f == b
_l_(13764)
True
_l_(13765)
b == f
_l_(13766)
False
_l_(13767)

def __eq__(self, other):
    _l_(13771)

    if type(other) is type(self):
        _l_(13769)

        aux = self.__dict__ == other.__dict__
        _l_(13768)
        return aux
    aux = False
    _l_(13770)
    return aux


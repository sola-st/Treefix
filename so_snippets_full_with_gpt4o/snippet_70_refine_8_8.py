a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'] # pragma: no cover
d = {} # pragma: no cover
a = type('Mock', (object,), {'count': lambda self, x: self.items.count(x)})() # pragma: no cover
a.items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'] # pragma: no cover

a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'] # pragma: no cover
d = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
from l3.Runtime import _l_
dict((i,a.count(i)) for i in a)
_l_(12781)

def occurDict(items):
    _l_(12787)

    d = {}
    _l_(12782)
    for i in items:
        _l_(12786)

        if i in d:
            _l_(12785)

            d[i] = d[i]+1
            _l_(12783)
        else:
            d[i] = 1
            _l_(12784)
aux = d
_l_(12788)
return aux


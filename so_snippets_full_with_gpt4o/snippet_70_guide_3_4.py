a = ['apple', 'banana', 'apple', 'orange'] # pragma: no cover
items = a # pragma: no cover
aux = {} # pragma: no cover

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


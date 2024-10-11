a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'] # pragma: no cover
d = Counter(a) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
from l3.Runtime import _l_
dict((i,a.count(i)) for i in a)
_l_(1155)

def occurDict(items):
    _l_(1161)

    d = {}
    _l_(1156)
    for i in items:
        _l_(1160)

        if i in d:
            _l_(1159)

            d[i] = d[i]+1
            _l_(1157)
        else:
            d[i] = 1
            _l_(1158)
aux = d
_l_(1162)
return aux


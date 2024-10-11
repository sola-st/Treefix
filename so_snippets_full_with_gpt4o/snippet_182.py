# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
from l3.Runtime import _l_
try:
    from collections import defaultdict
    _l_(11998)

except ImportError:
    pass

text = 'Mary had a little lamb'
_l_(11999)
chars = defaultdict(int)
_l_(12000)

for char in text:
    _l_(12002)

    chars[char] += 1
    _l_(12001)

chars['a']
_l_(12003)
4
_l_(12004)
chars['x']
_l_(12005)
0
_l_(12006)

class CICounter(defaultdict):
    _l_(12011)

    def __getitem__(self, k):
        _l_(12008)

        aux = super().__getitem__(k.lower())
        _l_(12007)
        return aux

    def __setitem__(self, k, v):
        _l_(12010)

        super().__setitem__(k.lower(), v)
        _l_(12009)


chars = CICounter(int)
_l_(12012)

for char in text:
    _l_(12014)

    chars[char] += 1
    _l_(12013)

chars['a']
_l_(12015)
4
_l_(12016)
chars['M']
_l_(12017)
2
_l_(12018)
chars['x']
_l_(12019)
0
_l_(12020)


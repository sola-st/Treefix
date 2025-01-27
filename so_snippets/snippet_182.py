# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
from l3.Runtime import _l_
try:
    from collections import defaultdict
    _l_(167)

except ImportError:
    pass

text = 'Mary had a little lamb'
_l_(168)
chars = defaultdict(int)
_l_(169)

for char in text:
    _l_(171)

    chars[char] += 1
    _l_(170)

chars['a']
_l_(172)
4
_l_(173)
chars['x']
_l_(174)
0
_l_(175)

class CICounter(defaultdict):
    _l_(180)

    def __getitem__(self, k):
        _l_(177)

        aux = super().__getitem__(k.lower())
        _l_(176)
        return aux

    def __setitem__(self, k, v):
        _l_(179)

        super().__setitem__(k.lower(), v)
        _l_(178)


chars = CICounter(int)
_l_(181)

for char in text:
    _l_(183)

    chars[char] += 1
    _l_(182)

chars['a']
_l_(184)
4
_l_(185)
chars['M']
_l_(186)
2
_l_(187)
chars['x']
_l_(188)
0
_l_(189)


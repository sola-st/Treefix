list_ = [1, 2, 2, 3, 4, 1, 5, 3] # pragma: no cover
key = lambda x: x # pragma: no cover

list_ = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape'] # pragma: no cover
key = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
"""efficient function to uniquify a list preserving item order"""
seen = set()
_l_(16208)
result = []
_l_(16209)
for item in list_:
    _l_(16215)

    seenkey = key(item)
    _l_(16210)
    if seenkey in seen:
        _l_(16212)

        continue
        _l_(16211)
    seen.add(seenkey)
    _l_(16213)
    result.append(item)
    _l_(16214)
aux = result
_l_(16216)
exit(aux)

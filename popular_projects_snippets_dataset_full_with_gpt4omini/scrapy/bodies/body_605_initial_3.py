list_ = [1, 2, 2, 3, 1, 4] # pragma: no cover
key = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
"""efficient function to uniquify a list preserving item order"""
seen = set()
_l_(4585)
result = []
_l_(4586)
for item in list_:
    _l_(4592)

    seenkey = key(item)
    _l_(4587)
    if seenkey in seen:
        _l_(4589)

        continue
        _l_(4588)
    seen.add(seenkey)
    _l_(4590)
    result.append(item)
    _l_(4591)
aux = result
_l_(4593)
exit(aux)

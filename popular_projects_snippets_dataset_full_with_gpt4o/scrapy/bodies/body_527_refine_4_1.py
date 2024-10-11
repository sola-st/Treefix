from time import time # pragma: no cover

live_refs = {type('A', (object,), {}): {1: 1660000000.0, 2: 1660000100.0}, type('B', (object,), {}): {3: 1660000200.0}} # pragma: no cover
ignore = (object,) # pragma: no cover

from time import time # pragma: no cover

class MockClass:# pragma: no cover
    __name__ = 'MockClass' # pragma: no cover
class IgnoreClass:# pragma: no cover
    pass # pragma: no cover
now = time() # pragma: no cover
live_refs = {MockClass: {1: now - 100, 2: now - 200}, IgnoreClass: {}} # pragma: no cover
ignore = (IgnoreClass,) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/trackref.py
from l3.Runtime import _l_
"""Return a tabular representation of tracked objects"""
s = "Live References\n\n"
_l_(21037)
now = time()
_l_(21038)
for cls, wdict in sorted(live_refs.items(),
                         key=lambda x: x[0].__name__):
    _l_(21045)

    if not wdict:
        _l_(21040)

        continue
        _l_(21039)
    if issubclass(cls, ignore):
        _l_(21042)

        continue
        _l_(21041)
    oldest = min(wdict.values())
    _l_(21043)
    s += f"{cls.__name__:<30} {len(wdict):6}   oldest: {int(now - oldest)}s ago\n"
    _l_(21044)
aux = s
_l_(21046)
exit(aux)

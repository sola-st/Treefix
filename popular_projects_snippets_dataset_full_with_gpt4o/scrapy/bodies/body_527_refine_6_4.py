from time import time # pragma: no cover

live_refs = {type('Mock', (object,), {}): {1: 1697044291, 2: 1697044200}, type('AnotherMock', (object,), {}): {3: 1697044190}} # pragma: no cover
ignore = (type('AnotherMock', (object,), {}),) # pragma: no cover

from time import time # pragma: no cover

current_time = time() # pragma: no cover
live_refs = {type('Mock', (object,), {}): {1: current_time - 100, 2: current_time - 200}, type('AnotherMock', (object,), {}): {3: current_time - 300}} # pragma: no cover
ignore = (object,) # pragma: no cover

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

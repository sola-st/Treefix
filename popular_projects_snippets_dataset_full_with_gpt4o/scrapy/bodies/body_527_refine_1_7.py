from time import time # pragma: no cover

live_refs = {type('MockClass', (object,), {'__name__': 'MockClass'}): {0: 1683019237, 1: 1683018237}, type('AnotherClass', (object,), {'__name__': 'AnotherClass'}): {2: 1683017237}} # pragma: no cover
ignore = (type('IgnoreClass', (object,), {}),) # pragma: no cover

from time import time, sleep # pragma: no cover

class MockClass:# pragma: no cover
    __name__ = 'MockClass'# pragma: no cover
    def __init__(self):# pragma: no cover
        self.timestamp = time() - 50# pragma: no cover
    def __call__(self):# pragma: no cover
        return self.timestamp # pragma: no cover
class AnotherClass:# pragma: no cover
    __name__ = 'AnotherClass'# pragma: no cover
    def __init__(self):# pragma: no cover
        self.timestamp = time() - 100# pragma: no cover
    def __call__(self):# pragma: no cover
        return self.timestamp # pragma: no cover
live_refs = {MockClass: {id(instance): instance() for instance in [MockClass(), MockClass()]},# pragma: no cover
             AnotherClass: {id(instance): instance() for instance in [AnotherClass()]}} # pragma: no cover
ignore = () # pragma: no cover
sleep(1) # pragma: no cover

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

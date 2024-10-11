from time import time # pragma: no cover

live_refs = {cls: {i: time() - i * 10 for i in range(5)} for cls in [int, str, list]} # pragma: no cover
ignore = object # pragma: no cover

from time import time # pragma: no cover

live_refs = {int: {1: time() - 100, 2: time() - 200}, str: {3: time() - 300}} # pragma: no cover
ignore = type('Ignore', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/trackref.py
from l3.Runtime import _l_
"""Return a tabular representation of tracked objects"""
s = "Live References\n\n"
_l_(9611)
now = time()
_l_(9612)
for cls, wdict in sorted(live_refs.items(),
                         key=lambda x: x[0].__name__):
    _l_(9619)

    if not wdict:
        _l_(9614)

        continue
        _l_(9613)
    if issubclass(cls, ignore):
        _l_(9616)

        continue
        _l_(9615)
    oldest = min(wdict.values())
    _l_(9617)
    s += f"{cls.__name__:<30} {len(wdict):6}   oldest: {int(now - oldest)}s ago\n"
    _l_(9618)
aux = s
_l_(9620)
exit(aux)

import re # pragma: no cover
from collections import defaultdict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile
from l3.Runtime import _l_
def match(pattern, string, flags=0):
    _l_(650)

    aux = _compile(pattern, flags).match(string)
    _l_(649)
    return aux

def _compile(*key):
    _l_(658)


    # Does cache check at top of function
    cachekey = (type(key[0]),) + key
    _l_(651)
    p = _cache.get(cachekey)
    _l_(652)
    if p is not None:
        _l_(653)

return p
    # ...
    # Does actual compilation on cache miss
    # ...

    # Caches compiled regex
    if len(_cache) >= _MAXCACHE:
        _l_(655)

        _cache.clear()
        _l_(654)
    _cache[cachekey] = p
    _l_(656)
    aux = p
    _l_(657)
    return aux


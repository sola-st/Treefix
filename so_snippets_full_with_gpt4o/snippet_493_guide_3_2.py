import re # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile
from l3.Runtime import _l_
def match(pattern, string, flags=0):
    _l_(12489)

    aux = _compile(pattern, flags).match(string)
    _l_(12488)
    return aux

def _compile(*key):
    _l_(12497)


    # Does cache check at top of function
    cachekey = (type(key[0]),) + key
    _l_(12490)
    p = _cache.get(cachekey)
    _l_(12491)
    if p is not None:
        _l_(12492)

return p
    # ...
    # Does actual compilation on cache miss
    # ...

    # Caches compiled regex
    if len(_cache) >= _MAXCACHE:
        _l_(12494)

        _cache.clear()
        _l_(12493)
    _cache[cachekey] = p
    _l_(12495)
    aux = p
    _l_(12496)
    return aux


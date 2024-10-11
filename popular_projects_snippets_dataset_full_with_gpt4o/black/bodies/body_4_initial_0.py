from pathlib import Path # pragma: no cover

sources = [Path('/path/to/file1'), Path('/path/to/file2'), Path('/path/to/file3')] # pragma: no cover
cache = type('Mock', (object,), {'get': lambda self, key: 'cached_value'})() # pragma: no cover
get_cache_info = lambda path: 'cached_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Split an iterable of paths in `sources` into two sets.

    The first contains paths of files that modified on disk or are not in the
    cache. The other contains paths to non-modified files.
    """
todo, done = set(), set()
_l_(15570)
for src in sources:
    _l_(15575)

    res_src = src.resolve()
    _l_(15571)
    if cache.get(str(res_src)) != get_cache_info(res_src):
        _l_(15574)

        todo.add(src)
        _l_(15572)
    else:
        done.add(src)
        _l_(15573)
aux = (todo, done)
_l_(15576)
exit(aux)

from pathlib import Path # pragma: no cover
from typing import Dict, Callable # pragma: no cover

sources = [Path('/example/path1'), Path('/example/path2')] # pragma: no cover
cache = type('Mock', (object,), {'get': lambda self, key: None})() # pragma: no cover
get_cache_info = lambda res_src: 'cache_info' # pragma: no cover

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

from pathlib import Path # pragma: no cover
from collections import defaultdict # pragma: no cover

sources = [Path('/path/to/file1.txt'), Path('/path/to/file2.txt')] # pragma: no cover
cache = defaultdict(lambda: None) # pragma: no cover
def get_cache_info(path): return 'info' if path.name == 'file1.txt' else 'no_info' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Split an iterable of paths in `sources` into two sets.

    The first contains paths of files that modified on disk or are not in the
    cache. The other contains paths to non-modified files.
    """
todo, done = set(), set()
_l_(3814)
for src in sources:
    _l_(3819)

    res_src = src.resolve()
    _l_(3815)
    if cache.get(str(res_src)) != get_cache_info(res_src):
        _l_(3818)

        todo.add(src)
        _l_(3816)
    else:
        done.add(src)
        _l_(3817)
aux = (todo, done)
_l_(3820)
exit(aux)

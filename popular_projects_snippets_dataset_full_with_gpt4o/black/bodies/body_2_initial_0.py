from pathlib import Path # pragma: no cover

CACHE_DIR = Path('/path/to/cache') # pragma: no cover
mode = type('Mock', (object,), {'get_cache_key': lambda self: 'default'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
aux = CACHE_DIR / f"cache.{mode.get_cache_key()}.pickle"
_l_(19243)
exit(aux)

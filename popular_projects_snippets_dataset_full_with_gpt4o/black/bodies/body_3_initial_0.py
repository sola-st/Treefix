from datetime import datetime # pragma: no cover
import os # pragma: no cover

path = type('Mock', (object,), {'stat': lambda: os.stat_result((0, 1, 2, 3, 4, 5, 1000, 7, int(datetime(2023, 1, 1).timestamp()), 0))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Return the information used to check if a file is already formatted or not."""
stat = path.stat()
_l_(15498)
aux = (stat.st_mtime, stat.st_size)
_l_(15499)
exit(aux)

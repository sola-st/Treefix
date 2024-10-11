from unittest.mock import MagicMock # pragma: no cover
import os # pragma: no cover
import time # pragma: no cover

path = MagicMock() # pragma: no cover
path.stat.return_value = os.stat_result((0, 0, 0, 0, 0, 0, 1024, time.time(), time.time(), time.time())) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Return the information used to check if a file is already formatted or not."""
stat = path.stat()
_l_(15498)
aux = (stat.st_mtime, stat.st_size)
_l_(15499)
exit(aux)

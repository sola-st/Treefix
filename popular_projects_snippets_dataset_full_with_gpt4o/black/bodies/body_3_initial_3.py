import os # pragma: no cover
import tempfile # pragma: no cover
import datetime # pragma: no cover

temp_dir = tempfile.TemporaryDirectory() # pragma: no cover
path = type('Mock', (object,), {'stat': lambda: os.stat(temp_dir.name)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/cache.py
from l3.Runtime import _l_
"""Return the information used to check if a file is already formatted or not."""
stat = path.stat()
_l_(15498)
aux = (stat.st_mtime, stat.st_size)
_l_(15499)
exit(aux)

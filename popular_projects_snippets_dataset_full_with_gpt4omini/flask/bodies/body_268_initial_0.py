import os # pragma: no cover

path = '/some/path/to/directory' # pragma: no cover
other = '/some/path/to/directory/file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Take ``other`` and remove the length of ``path`` from it. Then join it
    to ``path``. If it is the original value, ``path`` is an ancestor of
    ``other``."""
aux = os.path.join(path, other[len(path) :].lstrip(os.sep)) == other
_l_(6896)
exit(aux)

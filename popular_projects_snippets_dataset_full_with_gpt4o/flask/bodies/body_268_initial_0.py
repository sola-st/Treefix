import os # pragma: no cover

path = "/some/directory" # pragma: no cover
other = "/some/directory/subdirectory/file.txt" # pragma: no cover
os = type("Mock", (object,), {# pragma: no cover
    "path": type("MockPath", (object,), {# pragma: no cover
        "join": os.path.join# pragma: no cover
    }),# pragma: no cover
    "sep": os.sep# pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Take ``other`` and remove the length of ``path`` from it. Then join it
    to ``path``. If it is the original value, ``path`` is an ancestor of
    ``other``."""
aux = os.path.join(path, other[len(path) :].lstrip(os.sep)) == other
_l_(22746)
exit(aux)

import os # pragma: no cover
from typing import Any # pragma: no cover

mode = 'r' # pragma: no cover
self = type('Mock', (object,), {'root_path': '/path/to/resources'})() # pragma: no cover
resource = 'schema.sql' # pragma: no cover

import os # pragma: no cover

mode = 'r' # pragma: no cover
self = type('Mock', (object,), {'root_path': '.'})() # pragma: no cover
resource = 'schema.sql' # pragma: no cover
with open(resource, 'w') as f: f.write('-- SQL schema content --') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Open a resource file relative to :attr:`root_path` for
        reading.

        For example, if the file ``schema.sql`` is next to the file
        ``app.py`` where the ``Flask`` app is defined, it can be opened
        with:

        .. code-block:: python

            with app.open_resource("schema.sql") as f:
                conn.executescript(f.read())

        :param resource: Path to the resource relative to
            :attr:`root_path`.
        :param mode: Open the file in this mode. Only reading is
            supported, valid values are "r" (or "rt") and "rb".
        """
if mode not in {"r", "rt", "rb"}:
    _l_(6830)

    raise ValueError("Resources can only be opened for reading.")
    _l_(6829)
aux = open(os.path.join(self.root_path, resource), mode)
_l_(6831)

exit(aux)

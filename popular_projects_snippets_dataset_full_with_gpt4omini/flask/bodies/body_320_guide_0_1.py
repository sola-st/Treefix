import os # pragma: no cover
import contextlib # pragma: no cover

class MockApp(object): # pragma: no cover
    def __init__(self, root_path): # pragma: no cover
        self.root_path = root_path # pragma: no cover
    def open_resource(self, resource, mode): # pragma: no cover
        if mode not in {'r', 'rt', 'rb'}: # pragma: no cover
            raise ValueError('Resources can only be opened for reading.') # pragma: no cover
        return open(os.path.join(self.root_path, resource), mode) # pragma: no cover
 # pragma: no cover
app = MockApp(os.getcwd()) # pragma: no cover
resource = 'schema.sql' # pragma: no cover
mode = 'r' # pragma: no cover

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

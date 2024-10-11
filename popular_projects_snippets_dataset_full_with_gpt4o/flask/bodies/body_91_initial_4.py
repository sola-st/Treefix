import sys # pragma: no cover
import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The name of the application.  This is usually the import name
        with the difference that it's guessed from the run file if the
        import name is main.  This name is used as a display name when
        Flask needs the name of the application.  It can be set and overridden
        to change the value.

        .. versionadded:: 0.8
        """
if self.import_name == "__main__":
    _l_(22598)

    fn = getattr(sys.modules["__main__"], "__file__", None)
    _l_(22594)
    if fn is None:
        _l_(22596)

        aux = "__main__"
        _l_(22595)
        exit(aux)
    aux = os.path.splitext(os.path.basename(fn))[0]
    _l_(22597)
    exit(aux)
aux = self.import_name
_l_(22599)
exit(aux)

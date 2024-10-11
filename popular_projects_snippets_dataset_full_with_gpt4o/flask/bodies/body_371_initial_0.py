from types import SimpleNamespace # pragma: no cover

app = SimpleNamespace(config={'SESSION_COOKIE_HTTPONLY': True}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""Returns True if the session cookie should be httponly.  This
        currently just returns the value of the ``SESSION_COOKIE_HTTPONLY``
        config var.
        """
aux = app.config["SESSION_COOKIE_HTTPONLY"]
_l_(22560)
exit(aux)

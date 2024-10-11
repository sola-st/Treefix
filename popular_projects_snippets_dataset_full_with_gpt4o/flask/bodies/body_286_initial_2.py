import os # pragma: no cover

default = True # pragma: no cover
os.environ = type("Mock", (object,), {"get": lambda self, key: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Get whether the user has disabled loading default dotenv files by
    setting :envvar:`FLASK_SKIP_DOTENV`. The default is ``True``, load
    the files.

    :param default: What to return if the env var isn't set.
    """
val = os.environ.get("FLASK_SKIP_DOTENV")
_l_(20126)

if not val:
    _l_(20128)

    aux = default
    _l_(20127)
    exit(aux)
aux = val.lower() in ("0", "false", "no")
_l_(20129)

exit(aux)

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.get = lambda key, default: True if key == '_permanent' else default # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This reflects the ``'_permanent'`` key in the dict."""
aux = self.get("_permanent", False)
_l_(9108)
exit(aux)

from collections import defaultdict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.record_once = lambda func: func(None) # pragma: no cover
f = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Same as :meth:`url_value_preprocessor` but application wide."""
self.record_once(
    lambda s: s.app.url_value_preprocessors.setdefault(None, []).append(f)
)
_l_(8364)
aux = f
_l_(8365)
exit(aux)

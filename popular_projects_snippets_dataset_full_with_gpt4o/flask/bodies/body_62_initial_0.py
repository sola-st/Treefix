self = type('Mock', (object,), {'app': type('App', (object,), {'url_value_preprocessors': {}})(), 'record_once': lambda self, func: func(self)})() # pragma: no cover
f = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Same as :meth:`url_value_preprocessor` but application wide."""
self.record_once(
    lambda s: s.app.url_value_preprocessors.setdefault(None, []).append(f)
)
_l_(19496)
aux = f
_l_(19497)
exit(aux)

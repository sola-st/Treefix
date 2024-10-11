self = type('Mock', (object,), {'app': None})() # pragma: no cover
app = 'SampleApp' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/templating.py
from l3.Runtime import _l_
self.app = app
_l_(15872)

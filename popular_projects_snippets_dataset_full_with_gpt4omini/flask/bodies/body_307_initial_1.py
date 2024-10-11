import typing # pragma: no cover

self = type('Mock', (object,), {'_check_setup_finished': lambda f_name: None})() # pragma: no cover
f_name = 'setup_complete' # pragma: no cover
f = lambda self, *args, **kwargs: 'Function Executed' # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
self._check_setup_finished(f_name)
_l_(5569)
aux = f(self, *args, **kwargs)
_l_(5570)
exit(aux)

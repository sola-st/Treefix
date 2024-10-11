from typing import Callable, Any # pragma: no cover

self = type('Mock', (object,), {'_check_setup_finished': lambda f_name: print(f'Setup finished for {f_name}')})() # pragma: no cover
f_name = 'function_name' # pragma: no cover
f = lambda self, *args, **kwargs: 'Function executed' # pragma: no cover
args = (1, 2, 3) # pragma: no cover
kwargs = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
self._check_setup_finished(f_name)
_l_(5569)
aux = f(self, *args, **kwargs)
_l_(5570)
exit(aux)

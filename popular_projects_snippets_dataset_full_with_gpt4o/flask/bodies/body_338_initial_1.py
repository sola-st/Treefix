self = type('Mock', (object,), {'register_error_handler': lambda self, code_or_exception, f: None})() # pragma: no cover
code_or_exception = 1 # pragma: no cover
f = lambda: print('Error handler called') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
self.register_error_handler(code_or_exception, f)
_l_(15658)
aux = f
_l_(15659)
exit(aux)

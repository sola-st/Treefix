import logging # pragma: no cover

class Mock: # pragma: no cover
    def register_error_handler(self, code_or_exception, f): # pragma: no cover
        pass # pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
code_or_exception = 'ERROR_CODE_123' # pragma: no cover
f = lambda e: logging.error(f'Handled exception: {e}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
self.register_error_handler(code_or_exception, f)
_l_(4074)
aux = f
_l_(4075)
exit(aux)

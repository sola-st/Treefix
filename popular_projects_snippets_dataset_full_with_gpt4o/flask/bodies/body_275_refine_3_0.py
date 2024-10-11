err = Exception('An error occurred') # pragma: no cover

err = type('CustomError', (Exception,), {'__init__': lambda self: super(type(self), self).__init__('This is a custom error message')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)

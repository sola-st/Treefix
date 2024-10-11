class CustomError(Exception): pass # pragma: no cover
try: raise CustomError('An error occurred') # pragma: no cover
except CustomError as err: pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
raise err from None
_l_(16935)

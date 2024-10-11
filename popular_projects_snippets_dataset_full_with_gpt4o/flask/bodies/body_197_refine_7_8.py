args = (1,) # pragma: no cover
kwargs = {} # pragma: no cover

args = None # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if args and kwargs:
    _l_(17664)

    raise TypeError("app.json.response() takes either args or kwargs, not both")
    _l_(17663)

if not args and not kwargs:
    _l_(17666)

    aux = None
    _l_(17665)
    exit(aux)

if len(args) == 1:
    _l_(17668)

    aux = args[0]
    _l_(17667)
    exit(aux)
aux = args or kwargs
_l_(17669)

exit(aux)

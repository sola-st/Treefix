import sys # pragma: no cover

args = [1, 2, 3] # pragma: no cover
kwargs = {} # pragma: no cover

args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if args and kwargs:
    _l_(17530)

    raise TypeError("app.json.response() takes either args or kwargs, not both")
    _l_(17529)

if not args and not kwargs:
    _l_(17532)

    aux = None
    _l_(17531)
    exit(aux)

if len(args) == 1:
    _l_(17534)

    aux = args[0]
    _l_(17533)
    exit(aux)
aux = args or kwargs
_l_(17535)

exit(aux)

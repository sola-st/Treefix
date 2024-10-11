from typing import Any, List, Dict, Optional # pragma: no cover

args: List[Any] = [42] # pragma: no cover
kwargs: Dict[str, Any] = {} # pragma: no cover

args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if args and kwargs:
    _l_(6112)

    raise TypeError("app.json.response() takes either args or kwargs, not both")
    _l_(6111)

if not args and not kwargs:
    _l_(6114)

    aux = None
    _l_(6113)
    exit(aux)

if len(args) == 1:
    _l_(6116)

    aux = args[0]
    _l_(6115)
    exit(aux)
aux = args or kwargs
_l_(6117)

exit(aux)

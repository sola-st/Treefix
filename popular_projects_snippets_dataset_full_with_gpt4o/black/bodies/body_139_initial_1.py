from typing import List # pragma: no cover

value = '  Example line 1\n\nExample line 2  \n\nExample line 3\n  ' # pragma: no cover
lineend = '\n' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
# To normalize, we strip any leading and trailing space from
# each line...
from l3.Runtime import _l_
stripped: List[str] = [i.strip() for i in value.splitlines()]
_l_(19644)
normalized = lineend.join(stripped)
_l_(19645)
aux = normalized.strip()
_l_(19646)
# ...and remove any blank lines at the beginning and end of
# the whole string
exit(aux)

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
# To normalize, we strip any leading and trailing space from
# each line...
from l3.Runtime import _l_
stripped: List[str] = [i.strip() for i in value.splitlines()]
_l_(8189)
normalized = lineend.join(stripped)
_l_(8190)
aux = normalized.strip()
_l_(8191)
# ...and remove any blank lines at the beginning and end of
# the whole string
exit(aux)

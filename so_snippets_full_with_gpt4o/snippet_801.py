# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/363944/python-idiom-to-return-first-item-or-none
from l3.Runtime import _l_
first = lambda l, default=None: next(iter(l or []), default)
_l_(12050)


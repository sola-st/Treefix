import datetime # pragma: no cover
import operator # pragma: no cover

compare_operators_no_eq_ne = 'lt' # pragma: no cover
NaT = datetime.datetime.min # pragma: no cover
other = datetime.datetime.now() # pragma: no cover

import operator # pragma: no cover

compare_operators_no_eq_ne = 'lt' # pragma: no cover
class NaT: pass # pragma: no cover
other = NaT() # pragma: no cover
def compare_operators_no_eq_ne(self, other): return False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# GH 26039
from l3.Runtime import _l_
opname = compare_operators_no_eq_ne
_l_(4426)

assert getattr(NaT, opname)(other) is False
_l_(4427)

op = getattr(operator, opname.strip("_"))
_l_(4428)
assert op(NaT, other) is False
_l_(4429)
assert op(other, NaT) is False
_l_(4430)

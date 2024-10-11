import operator # pragma: no cover
import numpy as np # pragma: no cover

compare_operators_no_eq_ne = '__eq__' # pragma: no cover
NaT = np.datetime64('NaT') # pragma: no cover
other = np.datetime64('2023-10-01') # pragma: no cover
operator = type('MockOperator', (object,), {})() # pragma: no cover

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

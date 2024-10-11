import operator # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import NaT # pragma: no cover

compare_operators_no_eq_ne = 'ne' # pragma: no cover
other = pd.Timestamp('2022-01-01') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# GH 26039
from l3.Runtime import _l_
opname = compare_operators_no_eq_ne
_l_(15924)

assert getattr(NaT, opname)(other) is False
_l_(15925)

op = getattr(operator, opname.strip("_"))
_l_(15926)
assert op(NaT, other) is False
_l_(15927)
assert op(other, NaT) is False
_l_(15928)

# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

p1 = ArrowPeriodType("D")
p2 = ArrowPeriodType("D")
p3 = ArrowPeriodType("M")

assert p1.freq == "D"
assert p1 == p2
assert p1 != p3
assert hash(p1) == hash(p2)
assert hash(p1) != hash(p3)

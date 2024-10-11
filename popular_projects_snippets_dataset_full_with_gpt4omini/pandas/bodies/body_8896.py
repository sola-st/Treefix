# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
import pyarrow as pa

from pandas.core.arrays.arrow.extension_types import ArrowIntervalType

p1 = ArrowIntervalType(pa.int64(), "left")
p2 = ArrowIntervalType(pa.int64(), "left")
p3 = ArrowIntervalType(pa.int64(), "right")

assert p1.closed == "left"
assert p1 == p2
assert p1 != p3
assert hash(p1) == hash(p2)
assert hash(p1) != hash(p3)

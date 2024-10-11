from pandas import PeriodIndex, NaT, Period # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# monotonic
from l3.Runtime import _l_
idx1 = PeriodIndex([NaT, "2011-01-01", "2011-01-02", "2011-01-03"], freq="D")
_l_(15934)
assert not idx1.is_monotonic_increasing
_l_(15935)
assert idx1[1:].is_monotonic_increasing
_l_(15936)

# non-monotonic
idx2 = PeriodIndex(
    ["2011-01-01", NaT, "2011-01-03", "2011-01-02", NaT], freq="D"
)
_l_(15937)
assert not idx2.is_monotonic_increasing
_l_(15938)

for idx in [idx1, idx2]:
    _l_(15941)

    assert idx.min() == Period("2011-01-01", freq="D")
    _l_(15939)
    assert idx.max() == Period("2011-01-03", freq="D")
    _l_(15940)
assert idx1.argmin() == 1
_l_(15942)
assert idx2.argmin() == 0
_l_(15943)
assert idx1.argmax() == 3
_l_(15944)
assert idx2.argmax() == 2
_l_(15945)

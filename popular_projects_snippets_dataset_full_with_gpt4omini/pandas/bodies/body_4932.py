# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# monotonic
from l3.Runtime import _l_
idx1 = PeriodIndex([NaT, "2011-01-01", "2011-01-02", "2011-01-03"], freq="D")
_l_(4539)
assert not idx1.is_monotonic_increasing
_l_(4540)
assert idx1[1:].is_monotonic_increasing
_l_(4541)

# non-monotonic
idx2 = PeriodIndex(
    ["2011-01-01", NaT, "2011-01-03", "2011-01-02", NaT], freq="D"
)
_l_(4542)
assert not idx2.is_monotonic_increasing
_l_(4543)

for idx in [idx1, idx2]:
    _l_(4546)

    assert idx.min() == Period("2011-01-01", freq="D")
    _l_(4544)
    assert idx.max() == Period("2011-01-03", freq="D")
    _l_(4545)
assert idx1.argmin() == 1
_l_(4547)
assert idx2.argmin() == 0
_l_(4548)
assert idx1.argmax() == 3
_l_(4549)
assert idx2.argmax() == 2
_l_(4550)

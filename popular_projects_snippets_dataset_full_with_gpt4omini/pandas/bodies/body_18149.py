# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Tick
from l3.Runtime import _l_
other = three_days
_l_(5047)
rng = period_range("2014-05-01", "2014-05-15", freq="D")
_l_(5048)
expected = period_range("2014-05-04", "2014-05-18", freq="D")
_l_(5049)

result = rng + other
_l_(5050)
tm.assert_index_equal(result, expected)
_l_(5051)

rng += other
_l_(5052)
tm.assert_index_equal(rng, expected)
_l_(5053)

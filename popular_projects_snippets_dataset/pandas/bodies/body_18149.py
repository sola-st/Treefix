# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Tick
from l3.Runtime import _l_
other = three_days
_l_(16731)
rng = period_range("2014-05-01", "2014-05-15", freq="D")
_l_(16732)
expected = period_range("2014-05-04", "2014-05-18", freq="D")
_l_(16733)

result = rng + other
_l_(16734)
tm.assert_index_equal(result, expected)
_l_(16735)

rng += other
_l_(16736)
tm.assert_index_equal(rng, expected)
_l_(16737)

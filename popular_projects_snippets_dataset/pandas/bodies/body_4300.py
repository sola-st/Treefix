# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 13758
from l3.Runtime import _l_
data = {
    "One": Series(["A", 1.2, np.nan]),
}
_l_(20572)
df = DataFrame(data)
_l_(20573)
result = df.sum(axis=1)
_l_(20574)
expected = Series(["A", 1.2, 0])
_l_(20575)
tm.assert_series_equal(result, expected)
_l_(20576)

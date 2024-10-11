# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
from l3.Runtime import _l_
left = Series([np.inf, 1.0])
_l_(8742)
right = Series([np.inf, 2.0])
_l_(8743)

expected = left // right, left % right
_l_(8744)
result = divmod(left, right)
_l_(8745)

tm.assert_series_equal(result[0], expected[0])
_l_(8746)
tm.assert_series_equal(result[1], expected[1])
_l_(8747)

# rdivmod case
result = divmod(left.values, right)
_l_(8748)
tm.assert_series_equal(result[0], expected[0])
_l_(8749)
tm.assert_series_equal(result[1], expected[1])
_l_(8750)

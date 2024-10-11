# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
from l3.Runtime import _l_
left = Series([np.inf, 1.0])
_l_(20299)
right = Series([np.inf, 2.0])
_l_(20300)

expected = left // right, left % right
_l_(20301)
result = divmod(left, right)
_l_(20302)

tm.assert_series_equal(result[0], expected[0])
_l_(20303)
tm.assert_series_equal(result[1], expected[1])
_l_(20304)

# rdivmod case
result = divmod(left.values, right)
_l_(20305)
tm.assert_series_equal(result[0], expected[0])
_l_(20306)
tm.assert_series_equal(result[1], expected[1])
_l_(20307)

# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH: 6929
s = Series(np.random.rand(10))
expected = getattr(s.expanding(3), method)()
s = s + 5000
result = getattr(s.expanding(3), method)()
tm.assert_series_equal(result, expected)

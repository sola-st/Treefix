# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH3283
data = OrderedDict((f"col{i}", np.random.random()) for i in range(12))

series = Series(data)
expected = Series(list(data.values()), list(data.keys()))
tm.assert_series_equal(series, expected)

# Test with subclass
class A(OrderedDict):
    pass

series = Series(A(data))
tm.assert_series_equal(series, expected)

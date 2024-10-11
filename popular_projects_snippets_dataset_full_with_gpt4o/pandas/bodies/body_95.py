# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH#47527
mapping = defaultdict(int, {1: 10, np.nan: 42})
ser = Series([1, np.nan, 2])
result = ser.map(mapping)
expected = Series([10, 42, 0])
tm.assert_series_equal(result, expected)

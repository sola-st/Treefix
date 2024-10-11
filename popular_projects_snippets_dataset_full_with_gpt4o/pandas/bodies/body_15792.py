# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
dt64ser = Series(date_range("20130101", periods=3))
result = dt64ser.astype(object)
assert isinstance(result.iloc[0], datetime)
assert result.dtype == np.object_

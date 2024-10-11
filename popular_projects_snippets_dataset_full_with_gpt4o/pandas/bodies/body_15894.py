# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# GH#714 also, dtype=float
ser = Series([1.2345] * 100)
ser[::2] = np.nan
result = ser.unique()
assert len(result) == 2

# explicit f4 dtype
ser = Series([1.2345] * 100, dtype="f4")
ser[::2] = np.nan
result = ser.unique()
assert len(result) == 2

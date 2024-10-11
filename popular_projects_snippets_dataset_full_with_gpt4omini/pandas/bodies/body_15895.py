# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# NAs in object arrays GH#714
ser = Series(["foo"] * 100, dtype="O")
ser[::2] = np.nan
result = ser.unique()
assert len(result) == 2

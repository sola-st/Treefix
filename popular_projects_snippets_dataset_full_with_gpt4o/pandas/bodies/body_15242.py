# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_xs.py
# GH#31630 a case where we shouldn't wrap datetime64 in Timestamp
arr = date_range("2016-01-01", periods=3)._data._ndarray

ser = Series(arr, dtype=object)
for i in range(len(ser)):
    ser.iloc[i] = arr[i]
assert ser.dtype == object
assert isinstance(ser[0], np.datetime64)

result = ser.xs(0)
assert isinstance(result, np.datetime64)

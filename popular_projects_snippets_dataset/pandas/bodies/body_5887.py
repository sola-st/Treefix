# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
assert data[0] != data[1]
cls = type(data)
a, b = data[:2]

ser = pd.Series(cls._from_sequence([a, a, b, b], dtype=data.dtype))

cond = np.array([True, True, False, False])
result = ser.where(cond)

new_dtype = SparseDtype("float", 0.0)
expected = pd.Series(
    cls._from_sequence([a, a, na_value, na_value], dtype=new_dtype)
)
self.assert_series_equal(result, expected)

other = cls._from_sequence([a, b, a, b], dtype=data.dtype)
cond = np.array([True, False, True, True])
result = ser.where(cond, other)
expected = pd.Series(cls._from_sequence([a, b, b, b], dtype=data.dtype))
self.assert_series_equal(result, expected)

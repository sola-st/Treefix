# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH #37218
ser = Series([1, 2, 3])
key = np.array([4], dtype=any_unsigned_int_numpy_dtype)

with pytest.raises(KeyError, match="4"):
    ser[key]
with pytest.raises(KeyError, match="4"):
    ser.loc[key]

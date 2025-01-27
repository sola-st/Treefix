# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH#11343, added tests for hasnans / isnans
index = index_flat

# cases in indices doesn't include NaN
idx = index.copy(deep=True)
expected = np.array([False] * len(idx), dtype=bool)
tm.assert_numpy_array_equal(idx._isnan, expected)
assert idx.hasnans is False

idx = index.copy(deep=True)
values = idx._values

if len(index) == 0:
    exit()
elif isinstance(index, NumericIndex) and is_integer_dtype(index.dtype):
    exit()
elif index.dtype == bool:
    # values[1] = np.nan below casts to True!
    exit()

values[1] = np.nan

idx = type(index)(values)

expected = np.array([False] * len(idx), dtype=bool)
expected[1] = True
tm.assert_numpy_array_equal(idx._isnan, expected)
assert idx.hasnans is True

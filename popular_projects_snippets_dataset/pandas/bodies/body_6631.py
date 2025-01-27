# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH 26565, GH26617, GH35432
# This test checks whether _cache has been set.
# Calling RangeIndex._cache["_data"] creates an int64 array of the same length
# as the RangeIndex and stores it in _cache.
idx = RangeIndex(0, 100, 10)

assert idx._cache == {}

repr(idx)
assert idx._cache == {}

str(idx)
assert idx._cache == {}

idx.get_loc(20)
assert idx._cache == {}

90 in idx  # True
assert idx._cache == {}

91 in idx  # False
assert idx._cache == {}

idx.all()
assert idx._cache == {}

idx.any()
assert idx._cache == {}

for _ in idx:
    pass
assert idx._cache == {}

idx.format()
assert idx._cache == {}

df = pd.DataFrame({"a": range(10)}, index=idx)

str(df)
assert idx._cache == {}

df.loc[50]
assert idx._cache == {}

with pytest.raises(KeyError, match="51"):
    df.loc[51]
assert idx._cache == {}

df.loc[10:50]
assert idx._cache == {}

df.iloc[5:10]
assert idx._cache == {}

# idx._cache should contain a _data entry after call to idx._data
idx._data
assert isinstance(idx._data, np.ndarray)
assert idx._data is idx._data  # check cached value is reused
assert len(idx._cache) == 1
expected = np.arange(0, 100, 10, dtype="int64")
tm.assert_numpy_array_equal(idx._cache["_data"], expected)

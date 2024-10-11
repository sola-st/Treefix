# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series([], dtype=np.int64)
ser.index.name = "index_name"
ser = ser[ser.isna()]
assert ser.index.name == "index_name"
assert ser.dtype == np.int64

# GH#5877
# indexing with empty series
ser = Series(["A", "B"])
expected = Series(dtype=object, index=Index([], dtype="int64"))
result = ser[Series([], dtype=object)]
tm.assert_series_equal(result, expected)

# invalid because of the boolean indexer
# that's empty or not-aligned
msg = (
    r"Unalignable boolean Series provided as indexer \(index of "
    r"the boolean Series and of the indexed object do not match"
)
with pytest.raises(IndexingError, match=msg):
    ser[Series([], dtype=bool)]

with pytest.raises(IndexingError, match=msg):
    ser[Series([True], dtype=bool)]

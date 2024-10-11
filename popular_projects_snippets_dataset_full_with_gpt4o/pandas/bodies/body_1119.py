# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 7866
# multi-index slicing with missing indexers
idx = MultiIndex.from_product(
    [["A", "B", "C"], ["foo", "bar", "baz"]], names=["one", "two"]
)
ser = Series(np.arange(9, dtype="int64"), index=idx).sort_index()
expected = ser.iloc[pos]

if expected.size == 0 and indexer != []:
    with pytest.raises(KeyError, match=str(indexer)):
        ser.loc[indexer]
elif indexer == (slice(None), ["foo", "bah"]):
    # "bah" is not in idx.levels[1], raising KeyError enforced in 2.0
    with pytest.raises(KeyError, match="'bah'"):
        ser.loc[indexer]
else:
    result = ser.loc[indexer]
    tm.assert_series_equal(result, expected)

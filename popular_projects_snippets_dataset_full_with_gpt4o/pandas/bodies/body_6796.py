# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#41831
index = IntervalIndex([np.nan, Interval(1, 2), np.nan])

expected = np.array([True, False, True])
for key in [None, np.nan, NA]:
    assert key in index
    result = index.get_loc(key)
    tm.assert_numpy_array_equal(result, expected)

for key in [NaT, np.timedelta64("NaT", "ns"), np.datetime64("NaT", "ns")]:
    with pytest.raises(KeyError, match=str(key)):
        index.get_loc(key)

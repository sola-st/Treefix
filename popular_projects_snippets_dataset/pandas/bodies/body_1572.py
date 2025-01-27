# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#42055
lev1 = np.array([np.nan, np.nan])
lev2 = ["bar", "baz"]
mi = MultiIndex.from_arrays([lev1, lev2])
ser = Series([0, 1], index=mi)
result = ser.loc[:, "bar"]

# TODO: should we have name="bar"?
expected = Series([0], index=[np.nan])
tm.assert_series_equal(result, expected)

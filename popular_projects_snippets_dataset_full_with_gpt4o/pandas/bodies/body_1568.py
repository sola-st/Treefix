# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#47677
srs = Series(
    [1, 2, 3],
    dtype=CategoricalDtype(Index([1, 2, 3], dtype=any_numeric_ea_dtype)),
)
# enlarge
srs.loc[3] = np.nan
expected = Series(
    [1, 2, 3, np.nan],
    dtype=CategoricalDtype(Index([1, 2, 3], dtype=any_numeric_ea_dtype)),
)
tm.assert_series_equal(srs, expected)
# set into
srs.loc[1] = np.nan
expected = Series(
    [1, np.nan, 3, np.nan],
    dtype=CategoricalDtype(Index([1, 2, 3], dtype=any_numeric_ea_dtype)),
)
tm.assert_series_equal(srs, expected)

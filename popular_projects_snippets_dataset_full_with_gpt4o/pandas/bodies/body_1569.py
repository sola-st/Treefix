# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#47677
srs_enlarge = Series(["a", "b", "c"], dtype="category")
srs_enlarge.loc[3] = na

srs_setinto = Series(["a", "b", "c", "a"], dtype="category")
srs_setinto.loc[3] = na

tm.assert_series_equal(srs_enlarge, srs_setinto)
expected = Series(["a", "b", "c", na], dtype="category")
tm.assert_series_equal(srs_enlarge, expected)

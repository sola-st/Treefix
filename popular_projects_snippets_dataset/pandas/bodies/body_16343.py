# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 12948
data = {(1, 1, None): -1.0}
result = Series(data)
expected = Series(
    -1.0, index=MultiIndex(levels=[[1], [1], [np.nan]], codes=[[0], [0], [-1]])
)
tm.assert_series_equal(result, expected)

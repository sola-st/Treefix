# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_xs.py
# GH: 19056
mi = MultiIndex.from_tuples(
    [("a", "x"), ("a", "y"), ("b", "x")], names=["level1", "level2"]
)
ser = Series([1, 1, 1], index=mi)
result = ser.xs("a", axis=0, drop_level=False)
expected = Series(
    [1, 1],
    index=MultiIndex.from_tuples(
        [("a", "x"), ("a", "y")], names=["level1", "level2"]
    ),
)
tm.assert_series_equal(result, expected)

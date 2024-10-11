# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH#46900
pmidx = MultiIndex.from_arrays([[1], ["a"]], names=[("a", "b"), ("c", "d")])
result = pmidx.dtypes
expected = Series(
    ["int64", "object"], index=MultiIndex.from_tuples([("a", "b"), ("c", "d")])
)
tm.assert_series_equal(result, expected)

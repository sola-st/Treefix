# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH 46383
df = DataFrame(
    [["a", "x", "x"], ["b", "y", "y"], ["b", "y", "y"]],
    index=[0, 1, 1],
    columns=["c1", "c2", "c2"],
)
result = df.groupby(level=0).value_counts(subset=["c2"])
expected = Series(
    [1, 2],
    index=MultiIndex.from_arrays(
        [[0, 1], ["x", "y"], ["x", "y"]], names=[None, "c2", "c2"]
    ),
)
tm.assert_series_equal(result, expected)

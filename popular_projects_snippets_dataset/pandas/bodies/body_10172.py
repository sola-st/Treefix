# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 37641
# GH 38523: GH 37641 actually was not a bug.
# group_keys only applies to groupby.apply directly
arrays = [["val1", "val1", "val2"], ["val1", "val1", "val2"]]
index = MultiIndex.from_arrays(arrays, names=("idx1", "idx2"))

s = Series([1, 2, 3], index=index)
result = s.groupby(["idx1", "idx2"], group_keys=group_keys).rolling(1).mean()
expected = Series(
    [1.0, 2.0, 3.0],
    index=MultiIndex.from_tuples(
        [
            ("val1", "val1", "val1", "val1"),
            ("val1", "val1", "val1", "val1"),
            ("val2", "val2", "val2", "val2"),
        ],
        names=["idx1", "idx2", "idx1", "idx2"],
    ),
)
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
idx = Index(["some_equal_splits", "with_no_nans", np.nan, None])
result = idx.str.split("_", expand=True)
exp = MultiIndex.from_tuples(
    [
        ("some", "equal", "splits"),
        ("with", "no", "nans"),
        [np.nan, np.nan, np.nan],
        [None, None, None],
    ]
)
tm.assert_index_equal(result, exp)
assert result.nlevels == 3

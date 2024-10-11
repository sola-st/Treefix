# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame(
    {"key": ["a", "b", "c", "d", "e", "e", "a"], "v1": np.random.randn(7)}
)
right = DataFrame({"v2": np.random.randn(4)}, index=["d", "b", "c", "a"])

merged1 = merge(
    left, right, left_on="key", right_index=True, how="left", sort=False
)
merged2 = merge(
    right, left, right_on="key", left_index=True, how="right", sort=False
)
tm.assert_frame_equal(merged1, merged2.loc[:, merged1.columns])

merged1 = merge(
    left, right, left_on="key", right_index=True, how="left", sort=True
)
merged2 = merge(
    right, left, right_on="key", left_index=True, how="right", sort=True
)
tm.assert_frame_equal(merged1, merged2.loc[:, merged1.columns])

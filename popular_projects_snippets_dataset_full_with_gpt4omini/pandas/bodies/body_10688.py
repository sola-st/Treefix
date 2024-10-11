# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
df = DataFrame(
    {"key": ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b"], "val": [1] * 10}
)
result = df.groupby("key").rank(pct=pct)
exp_df = DataFrame(exp * 2, columns=["val"])
tm.assert_frame_equal(result, exp_df)

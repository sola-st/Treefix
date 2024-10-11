# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# GH 20561
key = np.repeat(grps, len(vals))
vals = vals * len(grps)
df = DataFrame({"key": key, "val": vals})
result = df.groupby("key").rank(
    method=ties_method, ascending=ascending, na_option=na_option
)
exp_df = DataFrame(exp * len(grps), columns=["val"])
tm.assert_frame_equal(result, exp_df)

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
df = DataFrame(
    {"cats": ["a", "b", "b", "a", "a", "d"], "vals": [1, 2, 3, 4, 5, 6]}
)
cats = Categorical(["a", "b", "b", "a", "a", "d"])
exp_df = DataFrame({"cats": cats, "vals": [1, 2, 3, 4, 5, 6]})
df["cats"] = df["cats"].astype("category")
tm.assert_frame_equal(exp_df, df)

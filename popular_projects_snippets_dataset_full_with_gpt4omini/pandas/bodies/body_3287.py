# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
df = DataFrame({"cats": [1, 2, 3, 4, 5, 6], "vals": [1, 2, 3, 4, 5, 6]})
cats = Categorical([1, 2, 3, 4, 5, 6])
exp_df = DataFrame({"cats": cats, "vals": [1, 2, 3, 4, 5, 6]})
df["cats"] = df["cats"].astype("category")
tm.assert_frame_equal(exp_df, df)

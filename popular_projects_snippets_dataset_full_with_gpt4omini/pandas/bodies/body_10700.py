# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
cat = pd.Categorical(["a", "a", "b", np.nan, "c", "b"], ordered=True)
cat2 = pd.Categorical([1, 2, 3, np.nan, 4, 5], ordered=True)

df = DataFrame({"col1": [0, 1, 0, 1, 0, 1], "col2": cat, "col3": cat2})

gb = df.groupby("col1")

res = gb.rank()

expected = df.astype(object).groupby("col1").rank()
tm.assert_frame_equal(res, expected)

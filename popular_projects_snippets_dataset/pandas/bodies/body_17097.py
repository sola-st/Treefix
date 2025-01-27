# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
cat = Categorical(["a", "b"], categories=["a", "b"])
vals = [1, 2]
df = DataFrame({"cats": cat, "vals": vals})
cat2 = Categorical(["a", "b", "a", "b"], categories=["a", "b"])
vals2 = [1, 2, 1, 2]
exp = DataFrame({"cats": cat2, "vals": vals2}, index=Index([0, 1, 0, 1]))

tm.assert_frame_equal(pd.concat([df, df]), exp)
tm.assert_frame_equal(df._append(df), exp)

# GH 13524 can concat different categories
cat3 = Categorical(["a", "b"], categories=["a", "b", "c"])
vals3 = [1, 2]
df_different_categories = DataFrame({"cats": cat3, "vals": vals3})

res = pd.concat([df, df_different_categories], ignore_index=True)
exp = DataFrame({"cats": list("abab"), "vals": [1, 2, 1, 2]})
tm.assert_frame_equal(res, exp)

res = df._append(df_different_categories, ignore_index=True)
tm.assert_frame_equal(res, exp)

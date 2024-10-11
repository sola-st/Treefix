# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_coercion.py
# fixed by GH#45121
orig = DataFrame({"A": [1, 2, 3], "B": [3, 4, 5]})
expected = DataFrame({"A": [1, 2, 3], "B": [3, 1.2, 5]})

df = orig.copy()
df.at[1, "B"] = 1.2
tm.assert_frame_equal(df, expected)

df = orig.copy()
df.loc[1, "B"] = 1.2
tm.assert_frame_equal(df, expected)

df = orig.copy()
df.iat[1, 1] = 1.2
tm.assert_frame_equal(df, expected)

df = orig.copy()
df.iloc[1, 1] = 1.2
tm.assert_frame_equal(df, expected)

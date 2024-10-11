# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39510
cols = ["A", "B"] * 2
df = DataFrame(0.0, index=[0], columns=cols)
df_copy = df.copy()
df_view = df[:]
df["B"] = (2, 5)

expected = DataFrame([[0.0, 2, 0.0, 5]], columns=cols)
tm.assert_frame_equal(df_view, df_copy)
tm.assert_frame_equal(df, expected)

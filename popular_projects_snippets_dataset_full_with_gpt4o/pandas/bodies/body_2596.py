# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39510
cols = ["A", "B"]
df = DataFrame(0, index=[0, 1], columns=cols)
df_copy = df.copy()
df_view = df[:]
df[["B"]] = value

expected = DataFrame([[0, 1.0], [0, 1.0]], columns=cols)
tm.assert_frame_equal(df_view, df_copy)
tm.assert_frame_equal(df, expected)

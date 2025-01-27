# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#49121
df = DataFrame({("a", "b"): [10]})
expected = df.copy()
col_name = ("a", "b")
df[col_name] = df[[col_name]]
tm.assert_frame_equal(df, expected)

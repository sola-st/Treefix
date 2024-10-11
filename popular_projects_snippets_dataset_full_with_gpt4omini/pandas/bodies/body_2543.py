# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#38604
df = DataFrame([[1, 2, 3]], columns=["a", "b", "b"])
rhs = DataFrame([[10, 11, 12]], columns=["a", "b", "b"])
df[["a", "b"]] = rhs
expected = DataFrame([[10, 11, 12]], columns=["a", "b", "b"])
tm.assert_frame_equal(df, expected)

df[["c", "b"]] = rhs
expected = DataFrame([[10, 11, 12, 10]], columns=["a", "b", "b", "c"])
tm.assert_frame_equal(df, expected)

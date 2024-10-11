# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 9428
expected = DataFrame(index=[0, 1], columns=[0, 1], dtype=object)

df = DataFrame(index=[0, 1], columns=[0, 1], dtype=str)
tm.assert_frame_equal(df, expected)
df = DataFrame(index=[0, 1], columns=[0, 1], dtype=np.str_)
tm.assert_frame_equal(df, expected)
df = DataFrame(index=[0, 1], columns=[0, 1], dtype=np.unicode_)
tm.assert_frame_equal(df, expected)
df = DataFrame(index=[0, 1], columns=[0, 1], dtype="U5")
tm.assert_frame_equal(df, expected)

# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# GH#39168
df = DataFrame([[0, 1, 2]], columns=["foo", "bar", 42], index=[1, "test", 2])
tm.assert_frame_equal(df, df, check_like=True)

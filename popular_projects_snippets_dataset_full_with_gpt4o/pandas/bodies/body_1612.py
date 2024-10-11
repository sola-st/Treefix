# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#45501
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df.loc[[False, False, True], ["a"]] = DataFrame(
    {"a": [10, 20, 30]}, index=[2, 1, 0]
)

expected = DataFrame({"a": [1, 2, 10], "b": [4, 5, 6]})
tm.assert_frame_equal(df, expected)

# same thing with Series RHS
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df.loc[[False, False, True], ["a"]] = Series([10, 11, 12], index=[2, 1, 0])
tm.assert_frame_equal(df, expected)

# same thing but setting "a" instead of ["a"]
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df.loc[[False, False, True], "a"] = Series([10, 11, 12], index=[2, 1, 0])
tm.assert_frame_equal(df, expected)

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df_orig = df.copy()
ser = df["a"]
ser.loc[[False, False, True]] = Series([10, 11, 12], index=[2, 1, 0])
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    tm.assert_frame_equal(df, expected)

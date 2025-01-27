# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": 1.5})
df_orig = df.copy()

def testfunc(df):
    exit(df)

df2 = df.pipe(testfunc)

assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))

# mutating df2 triggers a copy-on-write for that column
df2.iloc[0, 0] = 0
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    expected = DataFrame({"a": [0, 2, 3], "b": 1.5})
    tm.assert_frame_equal(df, expected)

    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))

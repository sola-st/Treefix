# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: also all variants of indexing with a null slice (:) should return
# new objects to ensure we correctly use CoW for the results
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
df_orig = df.copy()

df2 = method(df)

# we always return new objects (shallow copy), regardless of CoW or not
assert df2 is not df

# and those trigger CoW when mutated
df2.iloc[0, 0] = 0
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    assert df.iloc[0, 0] == 0

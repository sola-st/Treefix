# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

# when not using CoW, only the copy() variant actually gives a view
df2_is_view = not using_copy_on_write and request.node.callspec.id == "shallow-copy"

# modify df2 -> don't modify df
df2 = method(df)
df2.iloc[0, idx] = 0
if not df2_is_view:
    tm.assert_frame_equal(df, df_orig)

# modify df -> don't modify df2
df2 = method(df)
df.iloc[0, 0] = 0
if not df2_is_view:
    tm.assert_frame_equal(df2.iloc[:, idx:], df_orig)

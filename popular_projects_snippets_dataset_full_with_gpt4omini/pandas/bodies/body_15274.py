# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH 4080
df = DataFrame({c: [1, 2, 3] for c in ["a", "b", "c"]})
return_value = df.set_index(["a", "b", "c"], inplace=True)
assert return_value is None
s = Series([1], index=[(2, 2, 2)])
df["val"] = 0
df_original = df.copy()
df
df["val"].update(s)

if using_copy_on_write:
    expected = df_original
else:
    expected = DataFrame(
        {"a": [1, 2, 3], "b": [1, 2, 3], "c": [1, 2, 3], "val": [0, 1, 0]}
    )
    return_value = expected.set_index(["a", "b", "c"], inplace=True)
    assert return_value is None
tm.assert_frame_equal(df, expected)

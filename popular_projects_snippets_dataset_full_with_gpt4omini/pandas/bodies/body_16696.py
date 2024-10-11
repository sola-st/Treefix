# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
df = DataFrame({"key": [1, 2, 3], "v1": [4, 5, 6], "v2": [7, 8, 9]})
df2 = DataFrame({"key": [1, 2, 3], "v1": [4, 5, 6], "v2": [7, 8, 9]})

df.columns = ["key", "foo", "foo"]
df2.columns = ["key", "bar", "bar"]
expected = DataFrame(
    {
        "key": [1, 2, 3],
        "v1": [4, 5, 6],
        "v2": [7, 8, 9],
        "v3": [4, 5, 6],
        "v4": [7, 8, 9],
    }
)
expected.columns = ["key", "foo", "foo", "bar", "bar"]
tm.assert_frame_equal(merge(df, df2), expected)

# #2649, #10639
df2.columns = ["key1", "foo", "foo"]
msg = r"Data columns not unique: Index\(\['foo'\], dtype='object'\)"
with pytest.raises(MergeError, match=msg):
    merge(df, df2)
